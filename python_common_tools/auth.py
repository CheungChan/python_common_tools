# -*- coding: utf-8 -*-
__author__ = "陈章"
__date__ = "2019/11/25 14:20"
import base64
import hashlib
import hmac
import re
import time


class APIAuth:
    @classmethod
    def get_client_headers(cls, http_method, uri, client_id, client_secret) -> dict:
        gmt_time = str(int(time.time()))
        string2_sign = f"{http_method} {uri}\n{gmt_time}".encode("utf-8")
        signature = (
            base64.encodebytes(
                hmac.new(
                    client_secret.encode("utf-8"), string2_sign, hashlib.sha1
                ).digest()
            )
            .decode("utf-8")
            .replace("\n", "")
        )
        headers = {"Date": gmt_time, "Authorization": client_id + ":" + signature}
        return headers

    @classmethod
    def authenticate_at_server(
        cls, auth, client_id, client_secret, http_method, uri, gmttime
    ) -> (bool, str):
        if not auth or ":" not in auth:
            return False, f"auth format bad:::{auth}"
        auth_id = auth.split(":")[0].strip()
        if auth_id != client_id:
            return False, f"not exsit key:::{auth_id}"
        auth_str = auth.split(":")[1].strip()
        string2_sign = f"{http_method} {uri}\n{gmttime}".encode("utf-8")
        signature = (
            base64.encodebytes(
                hmac.new(
                    client_secret.encode("utf-8"), string2_sign, hashlib.sha1
                ).digest()
            )
            .decode("utf-8")
            .replace("\n", "")
        )
        if signature != auth_str:
            return False, "auth failed:::" + signature + ":::" + auth_str
        if re.match(r"^\d+$", gmttime):
            gmttime = int(gmttime)
            cur_timestamp = int(time.time())
            if gmttime < (cur_timestamp - 30) or gmttime > (cur_timestamp + 30):
                return (
                    False,
                    "auth failed for timestamp, cur_timestamp is:%s, auth timestamp is:%s"
                    % (cur_timestamp, gmttime),
                )
        return True, "ok"


if __name__ == "__main__":
    headers = APIAuth.get_client_headers(
        "POST", "/version/file/api", "xxx", "026e657b98646a2bc164c1d3b6280cc3"
    )
    print(headers)
    is_auth, msg = APIAuth.authenticate_at_server(
        headers["Authorization"],
        "xxx",
        "026e657b98646a2bc164c1d3b6280cc3",
        "POST",
        "/version/file/api",
        headers["Date"],
    )
    print(is_auth, msg)
