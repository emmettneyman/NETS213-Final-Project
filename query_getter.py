from __future__ import print_function
import json
import sys
import csv
import nltk
from random import randint
import re
import os
import numpy as np
import pandas as pd
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.externals import joblib
from sklearn.cluster import KMeans

os.system('clear')

json_data = open(sys.argv[1]).read()

data = json.loads(json_data)

output = {}

#Place Piazza posts into a dictionary
for elem in data:
     output[elem['history'][0]['subject'].encode('utf8').decode('utf8')] = elem['history'][0]['content'].encode('utf8').decode('utf8')

outputFile = open('simulated_data/query_list.csv','w')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['user_question_title','user_question_body'])

for key in output:
    outputWriter.writerow([unicode(key).encode('utf8'), unicode(output[key]).encode('utf8')])
outputFile.close()
