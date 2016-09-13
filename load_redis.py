# take a list of words, and save it to redis-db.
import sys
import numpy as np
import dill
import json
from redisdb import redis_store


if len(sys.argv) < 2:
    print '[usage] python load_redis <wordvec>'

vecs_path = sys.argv[1]
if len(sys.argv) >= 3:
    name = sys.argv[2]
else:
    name = 'word2vec'

print 'reading wordvec file'
with open(vecs_path, 'r') as f:
    while True:
        line = f.readline()
        line = line.replace('\n', '').strip()
        if not line:
            break
        line = line.split(' ')
        word = line[0]
        vec = [float(x) for x in line[1:]]
        redis_store.hset(name, word, json.dumps(vec))


