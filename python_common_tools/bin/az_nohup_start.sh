#!/usr/bin/env bash

proc=$@

help="阿章专用脚本:后台启动任务:$proc"

# 绿色输出提示
echo -e "\033[32m $help \033[0m"

# 将所有命令中的空格替换成_
# shell字符串替换用法  单个替换${variable/before/after}  全部替换 ${variable//before/after}
proc_no_blank=${proc//' '/'_'}
nohup $proc > "nohup.$proc_no_blank.out" 2>&1 &