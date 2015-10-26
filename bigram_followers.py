import nltk
import json
from collections import defaultdict
from nltk.util import ngrams

bigrams = ngrams(nltk.corpus.brown.words(), 2)
words = defaultdict(lambda : defaultdict(int))

for bigram in bigrams:
  score = 1
  if bigram[1] in [",", ".", "!", "''"]:
    score = 0.5

  words[bigram[0].lower()][bigram[1].lower()] += score

common_followers = {}
for word, followers in words.iteritems():
  followers = sorted(followers.keys(), key=lambda k: followers[k], reverse=True)[:10]
  common_followers[word] = followers

print json.dumps(common_followers)
