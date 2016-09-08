from redisdb import redis_store

test_words = '''album
brown
radio
super
china
likely
society
eyes
update
options
40
son
screen
engine
wrote
paul'''.split('\n')


for word in test_words:
  print redis_store.hget('word2vec', word)
  exit(0)
