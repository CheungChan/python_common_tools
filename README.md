## 一些常用的python工具箱

#### 安装
```bash
pip3 install python_common_tools 
```

#### 使用
```python


import time

# 使得函数使用缓存
from python_common_tools.cache import cache_function,cache_daily_function

@cache_function('.')
def f(self, a, b, c):
    time.sleep(3)
    return a + b + c
    
@cache_daily_function('.')
def f2(self, a, b, c):
    time.sleep(3)
    return a + b + c

# 快速设置日志
from python_common_tools.log import setup_logger

logger = setup_logger("test.log")


# 搞定异常处理的网络请求
from python_common_tools.network import secure_requests, secure_requests_json

resp = secure_requests("https://www.gethtml.com/test", retry_times=3,log_err=True)
j = secure_requests_json("https://www.getjson.com/test",timeout=10)

# linux系统相关的获取命令执行结果  获取最新版本号 打开远程服务器上的文件
from python_common_tools.linux import get_bash_output, get_latest_commit_id, open_remote_file

dirfiles = get_bash_output(["ls", "-l"])
commit_id = get_latest_commit_id()



```