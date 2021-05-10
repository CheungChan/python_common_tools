# -*- coding: utf-8 -*-
__author__ = "陈章"
__date__ = "2019/11/6 11:30"

import logging


logger = logging.getLogger("python_common_tools")


class RedisQueue(object):
    def __init__(self, key, host="localhost", port="6379", password="", db=0):
        import redis

        if not hasattr(RedisQueue, "pool"):
            RedisQueue.pool = redis.ConnectionPool(
                host=host, port=port, decode_responses=True, password=password, db=db
            )
        logger.info("get redis conn {host}:{port}".format(host=host, port=port))
        self.__db = redis.Redis(connection_pool=RedisQueue.pool)
        self.key = key

    def qsize(self):
        return self.__db.llen(self.key)

    def empty(self):
        return self.qsize() == 0

    def put(self, item):
        logger.info("put {key}: {item}".format(key=self.key, item=item))
        self.__db.rpush(self.key, item)

    def get(self, block=True, timeout=None):
        if block:
            item = self.__db.blpop(self.key, timeout=timeout)
        else:
            item = self.__db.lpop(self.key)

        if isinstance(item, tuple):
            item = item[1]
        logger.info("get {key}: {item}".format(key=self.key, item=item))
        return item

    def get_nowait(self):
        return self.get(False)
