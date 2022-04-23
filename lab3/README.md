# how to run

在项目目录：

1. `pip3 install flask`
2. 启动第一个服务器：`python3 app.py 8000`
3. 打开另一个终端，启动第二个服务器：`python3 app.py 8001`
4. 浏览器访问：`http://127.0.0.1:8000`

# 用到的技术

1. Python 使用 statsGen.py 生成 stats, 使用 flask 作为 http 服务器
2. HTML 使用 Ajax 请求 (XMLHttpRequest)，获取 python 端的 stats
3. Python 输出的 stats 为 JSON 格式
4. HTML 请求 8001 时，会遇到跨域问题，因此 Python 端的 stats 接口增加了 CORS 响应头（Access-Control-Allow-Origin 和
   Access-Control-Allow-Methods），允许跨域请求

具体代码作用，代码内有注释。