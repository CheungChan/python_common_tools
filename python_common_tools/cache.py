# -*- coding: utf-8 -*-
__author__ = '陈章'
__date__ = '2019-04-25 11:34'
import os
import pickle
from datetime import datetime
from functools import wraps
from urllib.parse import quote_plus

from logzero import logger

from python_common_tools.compress import get_md5


class Cache:

    @classmethod
    def cache_function(cls, cache_dir):
        def outer(f):
            @wraps(f)
            def inner(*args, **kwargs):
                fname = f.__qualname__
                argv_str = f'{quote_plus(str(args))}_{quote_plus(str(kwargs))}'
                cache_file = f'{cache_dir}/{fname}/{get_md5(argv_str)}.pkl'
                if not os.path.exists(cache_file):
                    if not os.path.exists(cache_dir):
                        os.mkdir(cache_dir)
                    if not os.path.exists(f'{cache_dir}/{fname}'):
                        os.mkdir(f'{cache_dir}/{fname}')
                    logger.debug(f'exec func {fname} {args} {kwargs}')
                    r = f(*args, **kwargs)
                    w_cache_file = open(cache_file, 'wb')
                    pickle.dump(r, w_cache_file)
                    w_cache_file.close()
                r_cache_file = open(cache_file, 'rb')
                r = pickle.load(r_cache_file)
                r_cache_file.close()
                return r

            return inner

        return outer

    @classmethod
    def cache_daily_function(cls, cache_dir):
        def outer(f):
            @wraps(f)
            def inner(*args, **kwargs):
                today = datetime.now().strftime("%Y%m%d")
                fname = f.__qualname__
                argv_str = f'{quote_plus(str(args))}_{quote_plus(str(kwargs))}'
                cache_file = f'{cache_dir}/{fname}/{today}/{get_md5(argv_str)}.pkl'
                if not os.path.exists(cache_file):
                    if not os.path.exists(cache_dir):
                        os.mkdir(cache_dir)
                    if not os.path.exists(f'{cache_dir}/{fname}'):
                        os.mkdir(f'{cache_dir}/{fname}')
                    if not os.path.exists(f'{cache_dir}/{fname}/{today}'):
                        os.mkdir(f'{cache_dir}/{fname}/{today}')
                    logger.debug(f'exec func {fname} {args} {kwargs}')
                    r = f(*args, **kwargs)
                    w_cache_file = open(cache_file, 'wb')
                    pickle.dump(r, w_cache_file)
                    w_cache_file.close()
                r_cache_file = open(cache_file, 'rb')
                r = pickle.load(r_cache_file)
                r_cache_file.close()
                return r

            return inner

        return outer


cache_function = Cache.cache_function
cache_daily_function = Cache.cache_daily_function
