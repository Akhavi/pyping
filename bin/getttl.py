import pyping
r = pyping.ping('8.8.8.8', udp = True, sourceaddress='10.10.10.10')
print r.ttl
print r.avg_rtt

r = pyping.ping('8.8.8.8', udp = True, sourceaddress='10.20.20.20')
print r.ttl
print r.avg_rtt

