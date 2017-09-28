import memcache
import time

client = memcache.Client([('127.0.0.1', 11211)])
sample_obj = {"name": "Soliman", "lang": "Python",
              "cluster": {'name': 'cluster_1', "content": '1234'}}
client.set("sample_user", sample_obj)
# print "Stored to memcached, will auto-expire after 5 seconds"
time.sleep(10)
sample_user = client.get("sample_user")
print sample_user
