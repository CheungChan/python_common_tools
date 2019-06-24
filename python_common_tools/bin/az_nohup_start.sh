#!/usr/bin/env bash

app_name=$1

help="阿章专用脚本:后台启动python脚本:$app_name"

# 绿色输出提示
echo -e "\033[32m $help \033[0m"

nohup python "$app_name" > "nohup.$app_name.out" 2>&1 &