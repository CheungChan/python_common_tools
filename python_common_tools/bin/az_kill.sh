#!/usr/bin/env bash

app_name=$1
help="阿章专用脚本:杀进程:$app_name"

# 绿色输出提示
echo -e "\033[32m $help \033[0m"
ps -ef|grep "$app_name" |grep -v "grep"| awk '{print $2}'| xargs kill
