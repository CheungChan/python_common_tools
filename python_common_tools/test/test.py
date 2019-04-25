# -*- coding: utf-8 -*-
__author__ = '陈章'
__date__ = '2019-04-25 10:58'

from python_common_tools.log import setup_logger
from python_common_tools.network import secure_get, secure_get_json
import unittest
import os


class TestLog(unittest.TestCase):

    def test_nofile_log(self):
        logger = setup_logger()
        logger.info("hello")
        logger.error("no")

    def test_log_file(self):
        logger = setup_logger("test.log")
        logger.info("hello")
        logger.error("no")
        os.remove("test.log")


class TestNetwork(unittest.TestCase):

    def setUp(self) -> None:
        self.logger = setup_logger()

    def test_secure_get_json(self):
        sample = 'db86e47238e15af467abbe55003b7912c41a9b08baad9d1d6e831b5785e463b8'
        url = f'https://s.threatbook.cn/api/v3/webpage/sandbox_type/{sample}'
        j = secure_get_json(url)
        self.logger.info(j)
        self.assertIsNotNone(j)

    def test_secure_get(self):
        url = 'https://www.baidu.com/'
        r = secure_get(url)
        self.logger.info(r.status_code)


if __name__ == '__main__':
    unittest.main()
