# rotating-proxy
A python module to automatically fetch rotating proxy ips.

# Sources
- https://free-proxy-list.net/

# Note
I would suggest to refresh the proxy list say around every 30min

```
rp_http = RotatingProxy(https = False)
rp_https.update()
```

# Install
```
pip install git+https://github.com/stamas02/rotating-proxy.git
```

# Usage
Here is an example code to repeatedly make a get request towards a pre-specified url 
using rotating proxy servers. 
```
import requests
from rotating_proxy.rotating_proxy import RotatingProxy

url = "http(s)://YOURURL.COM"
rp_http = RotatingProxy(https = False)
rp_https = RotatingProxy(https = True)
while True:
  rp_http.update()
  rp_https.update()
  for proxy_http , proxy_https  in zip(rp_http, rp_https):
    proxyDict = {"http"  : "{0}:{1}".format(*proxy_http[0:2]),
                 "https"  : "{0}:{1}".format(*proxy_https[0:2])}
    r = requests.get(url, proxies=proxyDict)
    print(r.text)
```
