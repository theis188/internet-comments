import urllib2
import json
from tproc import remHTML
import time
import nltk.stem.porter as porter
import nltk.stem.wordnet as wltz
import nltk.stem.snowball as snow

threads = json.load(urllib2.urlopen('https://a.4cdn.org/3/archive.json'))

time.sleep(1.5)
ps = porter.PorterStemmer()
wl = wltz.WordNetLemmatizer()
sb = snow.EnglishStemmer()

for i in range(1):

	url = 'https://a.4cdn.org/3/thread/'+str(threads[i])+'.json'

	dic = json.load(urllib2.urlopen(url))

	time.sleep(1.5)

	doc = ''

	for post in dic['posts']:
		try:
			doc+= remHTML(post['com']) + ' '
		except:
			True
	
	unigrams = [sb.stem(word) for word in doc.split()]

	wordcount = []

	for word in set(unigrams):
		wordcount.append( (unigrams.count(word), word) )
	print sorted(wordcount)