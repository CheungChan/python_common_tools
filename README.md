## 一些常用的python工具箱


防止各种异常出现的网络请求库
```python
from python_common_tools.network import secure_get,secure_get_json

j = secure_get_json("http://get_json.com/",{"k":"v"})
r = secure_get("http://get_text.com/",{"k":"v"})

```