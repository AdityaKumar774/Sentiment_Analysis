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

]