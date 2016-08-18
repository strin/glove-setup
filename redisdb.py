import redis
from os import environ

if 'REDIS_URL' in environ:
    redis_store = redis.StrictRedis.from_url(environ.get('REDIS_URL'))
else:
    redis_store = redis.StrictRedis(host='localhost', port=6379, db=0)
