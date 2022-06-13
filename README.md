# ipidea-proxy

Python library for ipidea proxy service API

## 使用客户端

#### 0. 安装

通过pip安装ipidea-proxy的python客户端

```shell
$ pip install --upgrade ipidea-proxy
Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple
Collecting ipidea-proxy
  Downloading https://pypi.tuna.tsinghua.edu.cn/packages/3a/65/b537feb63f22ce9453600cd49fbf1a230df6914c1ba133ed91efb1fa9a53/ipidea_proxy-0.5.0-py3-none-any.whl (7.8 kB)
Installing collected packages: ipidea-proxy
Successfully installed ipidea-proxy-0.5.0
```

#### 1. 获取UID和APPKEY

登录用户Profile

https://www.ipidea.net/ucenter/

然后访问API文档链接，从页面上获取UID和APPKEY

https://www.ipidea.net/ipidea-api.html#001

#### 2. 设置环境变量

通过上面获取的UID和APPKEY，设置到以下的环境变量。客户端会自动从该环境变量读取。

```shell
export IPIDEA_UID=xxx
export IPIDEA_APPKEY=xxx
```

#### 3. 初始化客户端

```shell
from ipidea_proxy import IpideaProxy

# 通过环境变量设置UID和APPKEY
# 如果UID和APPKEY已经通过环境变量设置，可以这样初始化客户端
ipp = IpideaProxy()

# 通过参数设置UID和APPKEY
ipp = IpideaProxy(uid='xxxx', appkey='xxxxxx')

```

#### 4. 使用客户端

##### 4.1 设置IP到白名单

```shell
# 添加本机公网IP到白名单
ipp.add_whitelist()

# 添加2.3.4.5到白名单
ipp.add_whitelist('2.3.4.5')
```

##### 4.2 从白名单中删除IP

```shell
# 从白名单中删除指定IP
ipp.delete_whitelist('2.3.4.5')

# 从白名单中删除本机对应公网IP
ipp.delete_whitelist()
```

## API Reference

https://www.ipidea.net/ipidea-api.html#001
