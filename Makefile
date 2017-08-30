all: redis glove word2vec

redis:
	sudo apt-get install -y redis-server
	sudo apt-get install -y python-pip
	sudo pip install -r requirements.txt
	sudo nohup redis-server &
	touch redis

glove:
	# sudo apt-get install -y unzip
	if [ ! -e "glove.zip" ] ; \
	then \
	    wget -O glove.zip http://nlp.stanford.edu/data/wordvecs/glove.42B.300d.zip; \
	fi;
	unzip glove.zip
	touch glove

# populate word vectors in db.
word2vec: 
	sudo apt-get install -y python-numpy
	python load_redis.py glove.42B.300d.txt
	touch word2vec

test:
	python test_redis.py

