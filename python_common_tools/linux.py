# -*- coding: utf-8 -*-
__author__ = '陈章'
__date__ = '2019-04-25 11:23'

import subprocess


class Bash:
    @classmethod
    def get_bash_output(cls, cmd_list):
        return subprocess.run(cmd_list, stdout=subprocess.PIPE).stdout.decode('utf-8')


class Git:
    @classmethod
    def get_latest_commit_id(cls):
        cmd = 'git rev-parse HEAD'
        return Bash.get_bash_output(cmd.split())


get_bash_output = Bash.get_bash_output

get_latest_commit_id = Git.get_latest_commit_id
