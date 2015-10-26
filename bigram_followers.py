import nltk
import json
from collections import defaultdict
from nltk.util import ngrams

bigrams = ngrams(nltk.corpus.brown.words(), 2)
words = defaultdict(lambda : defaultdict(int))

for bigram in bigrams:
  first_word = bigram[0].lower()
  second_word = bigram[1].lower()
  score = 1

  if second_word == "''" or second_word == '``':
    second_word = '"'

  if second_word in [',', '.', '!', '"']:
    score *= 0.5

  words[first_word][second_word] += score

common_followers = {}
for word, followers in words.iteritems():
  followers = sorted(followers.keys(), key=lambda k: followers[k], reverse=True)[:10]
  common_followers[word] = followers

print json.dumps(common_followers)
