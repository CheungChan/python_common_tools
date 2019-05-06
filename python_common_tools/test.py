# -*- coding: utf-8 -*-
__author__ = '陈章'
__date__ = '2019-04-25 10:58'

import os
import time
import shutil
import unittest

from python_common_tools.cache import cache_function
from python_common_tools.log import setup_logger
from python_common_tools.network import secure_requests, secure_requests_json
from python_common_tools.linux import get_bash_output, get_latest_commit_id, open_remote_file


class TestLog(unittest.TestCase):

    def test_nofile_log(self):
        logger = setup_logger()
        logger.info("hello")
        logger.error("no")

    def test_log_file(self):
        logger = setup_logger("test.log")
        logger.info("hello")
        logger.error("no")
        with open("test.log") as f:
            s = f.read()
            logger.info(f"The length of the logger file is {len(s)}")
            self.assertGreater(len(s), 0)
        os.remove("test.log")


class TestNetwork(unittest.TestCase):

    def setUp(self) -> None:
        self.logger = setup_logger()

    def test_secure_get_json(self):
        sample = 'db86e47238e15af467abbe55003b7912c41a9b08baad9d1d6e831b5785e463b8'
        url = f'https://s.threatbook.cn/api/v3/webpage/sandbox_type/{sample}'
        j = secure_requests_json(url)
        self.logger.info(j)
        self.assertIsNotNone(j)

    def test_secure_get(self):
        url = 'https://www.baidu.com/'
        r = secure_requests(url)
        self.logger.info(r.status_code)


class TestCache(unittest.TestCase):

    @cache_function
    def f(self, a, b, c):
        time.sleep(3)
        return a + b + c

    def test_cache_function(self):
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


class TestLinux(unittest.TestCase):

    def test_get_bash_output(self):
        output = get_bash_output(["echo", "hello"])
        self.assertEqual(output, "hello\n")

    def test_get_latest_commit_id(self):
        output = get_latest_commit_id()
        self.assertEqual(len(output.strip()), 40)

    def test_open_remote_file(self):
        pass


def main():
    unittest.main()


if __name__ == '__main__':
    main()
