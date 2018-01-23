import re
import json
from collections import Counter

emoticons_str = r"""
    (?:
       [:=;]
       [oO\-]?
       [D\)\]\(\]/\\OpP]
    )"""

regex_str = [
    emoticons_str,
    r'<[^>]+>',  # HTML tags
    r'(?:@[\w_]+)',  # mentions
    r"(?:\#+[\w_]+[\w\'_\-]'[\w_]+)",  # hash tags
    r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',  # urls
    r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and _
    r'(?:[\w_]+)',  # other words
    r'(?:\S)'  # every thing else
]

tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')', re.VERBOSE | re.IGNORECASE)
emoticons_re = re.compile(r'^' + emoticons_str + '$', re.VERBOSE | re.IGNORECASE)


def tokenize(s):
    return tokens_re.findall(s)


def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticons_re.search(token) else token.lower() for token in tokens]
    return tokens


from nltk.corpus import stopwords
import string

punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via']
fname = '/home/knight/PycharmProjects/Sentiment_Analysis/Twitter_Analysis/data.json'

with open(fname, 'r', newline='\r\n') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        # create a list with all the terms
        terms_stop = [term for term in preprocess(tweet['text']) if term not in stop]
        # count terms only once, equivalent to document frequency
        terms_single = set(terms_stop)
        # count hash tags only
        terms_hash = [term for term in preprocess(tweet['text']) if term.startswith('#')]
        # count term only (no hash tags, no mentions)
        terms_only = [term for term in preprocess(tweet['text'].lower()) if term not in stop]

        terms_all = [term for term in preprocess(tweet['text'])]
        # print all the terms

        new_terms = []
        for term in terms_only:
            if len(term) > 3:
                new_terms.append(term)

        count_all.update(new_terms)  # update the counter
    print(count_all.most_common(50))


import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import pandas as pd

data = count_all.most_common(50)
df = pd.DataFrame(data)
df.columns = ('terms', 'frec')
print(df.head())
word_string = ' '
for index, row in df.iterrows():
    word_string += (row['terms'] + ' ')*row['frec']

wordcloud = WordCloud(font_path='/home/knight/PycharmProjects/Sentiment_Analysis/Twitter_Analysis/Quesha.ttf',
                      stopwords=STOPWORDS,
                      background_color='white',
                      width=1200,
                      height=1000
                      ).generate(word_string)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()