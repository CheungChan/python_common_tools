#!/usr/bin/env bash

port=$1
src_path=$2
to_path=$3
help="阿章专用脚本:从ssh本地端口 $port 转发的 $src_path 拷贝文件到  $to_path"

# 绿色输出提示
echo -e "\033[32m $help \033[0m"
scp -r -P $port root@localhost:$src_path $to_path