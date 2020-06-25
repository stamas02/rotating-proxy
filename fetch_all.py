from rotating_proxy.rotating_proxy import RotatingProxy

rp = RotatingProxy()
for p in rp:
    print("{0}:{1}".format(*p[0:2]))