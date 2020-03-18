# -*- coding: utf-8 -*-
__author__ = "陈章"
__date__ = "2019-04-25 11:23"

import subprocess


class Bash:
    @classmethod
    def get_bash_output(cls, cmd_list):
        return subprocess.run(cmd_list, stdout=subprocess.PIPE).stdout.decode("utf-8")

    @classmethod
    def open_remote_file(cls, hostname, port, username, password, filename, mode="r"):
        import paramiko

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, port, username, password, compress=True)
        sftp_client = client.open_sftp()
        remote_file = sftp_client.open(filename, mode)
        return remote_file


class Git:
    @classmethod
    def get_latest_commit_id(cls):
        cmd = "git rev-parse HEAD"
        return Bash.get_bash_output(cmd.split())


class DownloadCode:
    @classmethod
    def download_code(cls):
        code = """
# save in web.py
# python >= 3.6
# pip install aiofiles fastapi uvicorn
import os

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse



app = FastAPI()

@app.get("/d/{p:path}")
async def download(p: str):
    if not os.path.exists(p):
        raise HTTPException(status_code=404, detail={"reason": f"{p}不存在","dir": os.path.abspath('.'), "files": os.listdir()})
    if not os.path.isfile(p):
        raise HTTPException(status_code=400, detail={"reason": f"{p}不是文件", "dir": os.path.abspath(p), "files": os.listdir(p)})
    return FileResponse(p)
if __name__ == '__main__':
    uvicorn.run("web:app", host='0.0.0.0', port=8002, reload=True)

"""
        print(code)


get_bash_output = Bash.get_bash_output
open_remote_file = Bash.open_remote_file
get_latest_commit_id = Git.get_latest_commit_id
download_code = DownloadCode.download_code
