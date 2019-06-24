#!/usr/bin/env bash

proc=$@

help="阿章专用脚本:后台启动任务:$proc"

# 绿色输出提示
echo -e "\033[32m $help \033[0m"

nohup python "$proc" > "nohup.$proc.out" 2>&1 &