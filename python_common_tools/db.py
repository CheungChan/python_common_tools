# -*- coding: utf-8 -*-
__author__ = "陈章"
__date__ = "2020/4/13 18:57"


class Cursor:
    def __init__(self, pool):
        self.pool = pool

    def __enter__(self):
        self.conn = self.pool.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.conn.close()


def get_pymysql_pool(host, port, user, passwd, db, charset, mincached=5):
    import pymysql
    from DBUtils.PooledDB import PooledDB

    pool = PooledDB(
        pymysql,
        mincached=mincached,
        host=host,
        port=port,
        user=user,
        passwd=passwd,
        db=db,
        charset=charset,
        cursorclass=pymysql.cursors.DictCursor,
    )
    return pool
