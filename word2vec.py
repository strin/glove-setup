# take a list of words, create a dictionary word -> vec.
import sys
import numpy as np
import dill

if len(sys.argv) < 4:
    print '[usage] python word2vec <vocab> <wordvec> <output>'

words_path = sys.argv[1]
vecs_path = sys.argv[2]
output_path = sys.argv[3]

with open(words_path, 'r') as f:
    words = f.readlines()

result = {}
wordvec = {}

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
        vec = np.array(vec, dtype=np.float32)
        wordvec[word] = vec

print 'creating custom dict'
for word in words:
    word = word.replace('\n', '')
    if not word:
        continue
    if word not in wordvec:
        word = '<unk>'
    result[word] = wordvec[word]

with open(output_path, 'w') as f:
    dill.dump(result, f)
