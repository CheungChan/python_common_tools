# -*- coding: utf-8 -*-
__author__ = '陈章'
__date__ = '2019-04-24 19:39'
import time
from json.decoder import JSONDecodeError

import requests
from logzero import logger
from requests.exceptions import ReadTimeout, ConnectionError


class IRequest:
    RETRY_TIMES = 3

    @classmethod
    def secure_get_json(cls, url, params=None, timeout=10, log_err=False):
        retry = IRequest.RETRY_TIMES
        j = {}
        while True:
            try:
                response = requests.get(url, params=params, timeout=timeout)
                j = response.json()
                break
            except ReadTimeout as e:
                if log_err:
                    logger.exception(e)
                time.sleep(2)
                retry -= 1
                if retry < 0:
                    break
                logger.error(f"url={url},params={params} ReadTimeout retrying {retry}")
            except ConnectionError as e:
                if log_err:
                    logger.exception(e)
                time.sleep(2)
                retry -= 1
                if retry < 0:
                    break
                logger.error(f"url={url},params={params} ConnectionError retrying {retry}")
            except JSONDecodeError as e:
                if log_err:
                    logger.exception(e)
                time.sleep(2)
                retry -= 1
                if retry < 0:
                    break
                logger.error(f"url={url},params={params} JSONDecodeError retrying {retry}")
        return j

    @classmethod
    def secure_get(cls, url, params=None, timeout=10, log_err=False):
        retry = IRequest.RETRY_TIMES
        response = None
        while True:
            try:
                response = requests.get(url, params=params, timeout=timeout)
                break
            except ReadTimeout as e:
                if log_err:
                    logger.exception(e)
                time.sleep(2)
                retry -= 1
                if retry < 0:
                    break
                logger.error(f"url={url},params={params} ReadTimeout retrying {retry}")
            except ConnectionError as e:
                if log_err:
                    logger.exception(e)
                time.sleep(2)
                retry -= 1
                if retry < 0:
                    break
                logger.error(f"url={url},params={params} ConnectionError retrying {retry}")
        return response
