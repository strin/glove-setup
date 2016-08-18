# take a list of words, and save it to redis-db.
import sys
import numpy as np
import dill
import json
from redisdb import redis_store

redis_store.delete('word2vec')
