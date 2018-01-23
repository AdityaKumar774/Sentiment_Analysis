import re
import json
from collections import Counter

emoticons_str = r"""
    (?:
       [:=;]    #Eyes
       [oO\-]?  #Nose
       [D\)\]\(\]/\\OpP]  #Mouth
    )"""

regex_str = [
    emoticons_str,
    
]