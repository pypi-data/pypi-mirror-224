import mongodbproxyutil
import mongodbproxyutil as PrivateProxyDataBaseUtil
proxydb = PrivateProxyDataBaseUtil.mongodb('192.168.20.254:27017','ProxyDB', 'PrivateProxy')


print(proxydb.get_all_proxies())