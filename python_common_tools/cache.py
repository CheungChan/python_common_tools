# -*- coding: utf-8 -*-
__author__ = '陈章'
__date__ = '2019-04-25 11:34'
import os
import pickle
from functools import wraps
from urllib.parse import quote_plus

from python_common_tools.compress import get_md5
from inspect import isfunction
from logzero import logger

class Cache:
    DEFAUT_CACHE_DIR = os.path.abspath(os.path.dirname(__file__))

    @classmethod
    def cache_function(cls, f):
        @wraps(f)
        def inner(*args, **kwargs):
            if 'cache_dir' not in kwargs:
                cache_dir = cls.DEFAUT_CACHE_DIR
            else:
                cache_dir = kwargs['cache_dir']
            fname = f.__qualname__
            cache_file = f'{cache_dir}/{fname}/' + get_md5(
                f'{quote_plus(str(args))}_{quote_plus(str(kwargs))}.pkl')
            if not os.path.exists(cache_file):
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


cache_function = Cache.cache_function
