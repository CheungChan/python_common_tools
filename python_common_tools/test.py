# -*- coding: utf-8 -*-
__author__ = "陈章"
__date__ = "2019-04-25 10:58"

import os
import shutil
import time
import unittest

from python_common_tools.cache import (
    cache_function,
    cache_daily_function,
    is_cache_or_not,
)
from python_common_tools.linux import get_bash_output, get_latest_commit_id
from python_common_tools.network import secure_requests, secure_requests_json
import logging


class TestNetwork(unittest.TestCase):
    def setUp(self) -> None:
        self.logger = logging.getLogger("python_common_tools.test")

    def test_secure_get_json(self):
        url = "https://m.douban.com/j/puppy/frodo_landing?include=anony_home"
        j = secure_requests_json(url)
        self.logger.info(j)
        self.assertIsNotNone(j)

    def test_secure_get(self):
        url = "https://www.baidu.com/"
        r = secure_requests(url)
        self.logger.info(r.status_code)


@cache_function(".")
def f(a, b, c):
    time.sleep(3)
    return a + b + c


@cache_daily_function(".")
def f2(a, b, c):
    time.sleep(3)
    return a + b + c


class TestCache(unittest.TestCase):
    @cache_function(".", is_method=True)
    def f(self, a, b, c):
        time.sleep(3)
        return a + b + c

    @cache_daily_function(".", is_method=True)
    def f2(self, a, b, c):
        time.sleep(3)
        return a + b + c

    def test_cache_function(self):
        begin = time.time()
        r1 = f(1, 2, 3)
        end = time.time()
        t1 = end - begin
        begin = time.time()

        r2 = f(1, 2, 3)
        shutil.rmtree("f")
        end = time.time()
        t2 = end - begin
        self.assertEqual(r1, 6)
        self.assertEqual(r2, 6)
        self.assertGreater(t1, t2)
        self.assertAlmostEqual(t1, 3.0, places=0)
        self.assertNotAlmostEqual(t2, 3.0, places=0)

        begin = time.time()
        r1 = self.f(1, 2, 3)
        end = time.time()
        t1 = end - begin
        begin = time.time()

        r2 = self.f(1, 2, 3)
        shutil.rmtree("TestCache.f")
        end = time.time()
        t2 = end - begin
        self.assertEqual(r1, 6)
        self.assertEqual(r2, 6)
        self.assertGreater(t1, t2)
        self.assertAlmostEqual(t1, 3.0, places=0)
        self.assertNotAlmostEqual(t2, 3.0, places=0)

    def test_cache_daily_function(self):
        begin = time.time()
        r1 = self.f2(1, 2, 3)
        end = time.time()
        t1 = end - begin
        begin = time.time()

        r2 = self.f2(1, 2, 3)
        shutil.rmtree("TestCache.f2")
        end = time.time()
        t2 = end - begin
        self.assertEqual(r1, 6)
        self.assertEqual(r2, 6)
        self.assertGreater(t1, t2)
        self.assertAlmostEqual(t1, 3.0, places=0)
        self.assertNotAlmostEqual(t2, 3.0, places=0)

    @is_cache_or_not(".", is_method=True)
    def f3(self, a):
        print("a=" + str(a))

    def test_is_cache_or_not(self):
        b = self.f3(1)
        self.assertFalse(b)
        b = self.f3(1)
        self.assertTrue(b)
        shutil.rmtree("TestCache.f3")


class TestLinux(unittest.TestCase):
    def test_get_bash_output(self):
        output = get_bash_output(["echo", "hello"])
        self.assertEqual(output, "hello\n")

    def test_get_latest_commit_id(self):
        output = get_latest_commit_id()
        self.assertEqual(len(output.strip()), 40)

    def test_open_remote_file(self):
        pass


def test_func1(i):
    return i


def test_func2(i, j):
    return i * j


def test_callback_func(i, r, callback_func_extra_kwargs):
    logger = callback_func_extra_kwargs["logger"]
    logger.info("i={i},r={r}".format(i=i, r=r))


def main():
    unittest.main()


if __name__ == "__main__":
    main()
