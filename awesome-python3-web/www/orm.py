#!usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'GuangHua Cao'
import asyncio, logging
import aiomysql

def log(sql, args=()):
    logging.info('SQL:%s' %sql)

async def create_pool(loop, **kw):
    logging.info('create database connection pool...')
    global __pool
    __pool = await aiomysql.create_pool(
        host=kw.get('host','localhost'),
        port=kw.get('post',3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset','utf-8'),
        autocommit=kw.get('autocommit',True),
        maxsize=kw.get('maxsize',10),
        minsize=kw.get('minsize',1),
        loop=loop
    )

async def select(sql, args, size=None):
    log(sql,args)
    global __pool
    async with __pool.get() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(sql.replace('?','%s'),args or ())
            if size:
                rs= await cur.fetchmany(size)
            else:
                rs = await cur.fetchall()
        logging.info('rows returned: %s' %len(rs))
        return rs

async def excute(sql, args, autocommit=True):
    log(sql)
    async with __pool.get() as conn:
        if not autocommit:
            await conn.begin()
        try:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                await cur.execute(sql.replace('?', '%s'), args)
                affected = cur.rowcount
            if not autocommit:
                await conn.commit()
        except BaseException as e:
            if not autocommit:
                await conn.rollback()
            raise
        return affected

def create_args_string(num):
    L = []
    for n in range(num):
        L.append('?')
    return ','.join(L)

class Field(object):
    def __init__(self,name,column_type, primary_key, default):
        self.name = name
        self.column_type = column_type
        self.primary_key = primary_key
        self.default = default

    def __str__(self):
        return '<%s,%s,%s:%s>' %(self.__class__,__name__,self.column_type,self.name)

class StringField(Field):
    def __init__(self, name=None, primary_key=False,default=None,ddl='varchar(100)'):
        super().__init__(name,ddl,primary_key,default)

class BooleanField(Field):
    def __init__(self,name=None,default=False):
        super().__init__(name,'boolean',False,default)

class IntegerField(Field):
    def __init__(self,name=None,primary_key=False,default=0):
        super().__init__(name,'bigint',False,default)

class FloatField(Field):
    def __init__(self,name=None,primary_key=False,default=0):
        super().__init__(name,'real',primary_key,default)

class TextField(Field):
    def __init__(self,name=None,default=None):
        super().__init__(name,'text',False,default)

class ModelMetaclass(type):
    def __new__(cls,name,bases,attrs):
        if name == 'Model':
            return type.__new__(cls,name,bases,attrs)
        tableName = attrs.get('__table__',None)
        logging.info('found model: %s (table %s)' % (name,tableName))
        mappings = dict()
        fields = []
        primaryKey = None

        for k,v in attrs.items():
            if isinstance(v,Field):
                logging.info(' Found mapping: %s ==> %s' %(k,v))
                mappings[k] = v
                if v.primary_key:
                    #找到主键
                    if primaryKey:
                        raise StandardError('Dulicate primary key for field: %s' %k)
                    primaryKey = k
                else:
                    fields.append(k)
            if not primaryKey:
                raise StandardError('Primary key not found.')
            for k in mappings.keys():
                attrs.pop(k)
            escaped_fields = list(map(lambda f: '`%s`' %f, fields))
            attrs['__mapping__'] = mappings #保存属性和列的映射关系
            attrs['__table__']  = tableName
            attrs['__primary_key__'] = primaryKey #主键属性名
            attrs['__fields__']



