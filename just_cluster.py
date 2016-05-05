from __future__ import print_function
import json
import sys
import csv
import nltk
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
#Remove stop-words and create tokens for the stems
stopwords = nltk.corpus.stopwords.words('english')

stemmer = SnowballStemmer("english")

RESULTS_NUM_TO_DISPLAY = 5
# here I define a tokenizer and stemmer which returns the set of stems in the text that it is passed

def tokenize_and_stem(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    stems = [stemmer.stem(t) for t in filtered_tokens]
    return stems


def tokenize_only(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    return filtered_tokens

totalvocab_stemmed = []
totalvocab_tokenized = []
for i in output:
    allwords_stemmed = tokenize_and_stem(output[i]) #for each item in 'synopses', tokenize/stem
    totalvocab_stemmed.extend(allwords_stemmed) #extend the 'totalvocab_stemmed' list
    
    allwords_tokenized = tokenize_only(output[i])
    totalvocab_tokenized.extend(allwords_tokenized)

print('FINISHED TOKENIZING')
vocab_frame = pd.DataFrame({'words': totalvocab_tokenized}, index = totalvocab_stemmed)
#print "there are " + str(vocab_frame.shape[0]) + ' items in vocab_frame'

#Compute tf-idf for each document

#define vectorizer parameters
tfidf_vectorizer = TfidfVectorizer(max_df=0.5, max_features=500000,
                                 min_df=0.001, stop_words='english',
                                 use_idf=True, tokenizer=tokenize_and_stem, ngram_range=(1,3))

tfidf_matrix = tfidf_vectorizer.fit_transform(output) #fit the vectorizer to synopses

print('FINISHED TF-IDF MATRIX')
print(tfidf_matrix.shape)
terms = tfidf_vectorizer.get_feature_names()

dist = 1 - cosine_similarity(tfidf_matrix)

#Run clustering algorithm (k-means)

num_clusters = 30

km = KMeans(n_clusters=num_clusters)

km.fit(tfidf_matrix)

clusters = km.labels_.tolist()

#uncomment the below to save your model 
#since I've already run my model I am loading from the pickle

joblib.dump(km,  'doc_cluster.pkl')

km = joblib.load('doc_cluster.pkl')
clusters = km.labels_.tolist()

posts = { 'title': output.keys(), 'body': output.values(), 'cluster': clusters }

frame = pd.DataFrame(posts, index = [clusters] , columns = [ 'title', 'body', 'cluster'])

frame['cluster'].value_counts() #number of films per cluster (clusters from 0 to 4)


#grouped = frame['title'].groupby(frame['cluster']) #groupby cluster for aggregation purposes

#grouped.mean() #average rank (1 to 100) per cluster

print("Top terms per cluster:")
print()
#sort cluster centers by proximity to centroid
clusters = []
order_centroids = km.cluster_centers_.argsort()[:, ::-1] 

for i in range(num_clusters):
    print()
    print("Cluster %d words:" % i, end='')
    words = []
    for ind in order_centroids[i, :6]: #replace 6 with n words per cluster
        print(' %s' % vocab_frame.ix[terms[ind].split(' ')].values.tolist()[0][0].encode('utf-8', 'ignore'), end=',')
        words.append('%s' % vocab_frame.ix[terms[ind].split(' ')].values.tolist()[0][0].encode('utf-8', 'ignore'))
 
    print() #add whitespace
    print() #add whitespace
    
    print("Cluster %d titles:" % i, end='')
    titles = []
    try:
	    for title in frame.ix[i]['title'].values.tolist():
	        print(' %s,' % title, end='')
	        titles.append(title)
	    clusters.append({'words': words, 'titles': titles})
	    # print() #add whitespace
	    # print() #add whitespace
    except:
		break
    
# print()
# print()
#Profit
