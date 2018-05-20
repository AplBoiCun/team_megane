import sys
import collections
import dbm
import json
import re

from tinydb import TinyDB, Query

from janome.tokenizer import Tokenizer
import termextract.janome
import termextract.core


if __name__ == "__main__":
  db = TinyDB('tweet_db.json')
  text = ""
  for i in db:
    text = text + i["text"]
  t = Tokenizer()
  tokenize_text = t.tokenize(text)
  frequency = termextract.janome.cmp_noun_dict(tokenize_text)
  #term_list = termextract.janome.cmp_noun_list(tagged_text)
  lr = termextract.core.score_lr(
      frequency,
      ignore_words=termextract.janome.IGNORE_WORDS,
      lr_mode=1, average_rate=1)
  data = termextract.core.term_importance(frequency, lr)
  data_collection = collections.Counter(data)
  for cmp_noun, value in data_collection.most_common():
    keyword = termextract.core.modify_agglutinative_lang(cmp_noun)
    if keyword.count("@") + keyword.count("RT") + keyword.count("http"):
      continue
    else:
      if value > 3:
        print(termextract.core.modify_agglutinative_lang(
            cmp_noun) + " " + str(value))
