#!/usr/bin/env python
# unweave.py
#
#
# Title:        Parsing wmata tweets and mining for signal
# Author:       Rebecca Bilbro
# Version:      1.0
# Date:         last updated 5/16/16
# Organization: Commerce Data Service, U.S. Department of Commerce


#####################################################################
# Imports
#####################################################################
from __future__ import print_function

import json
from sklearn.cluster import KMeans
from sklearn.cluster import MiniBatchKMeans
from sklearn.feature_extraction.text import TfidfVectorizer

#####################################################################
# Clusterize
#####################################################################
def clusterize(content, k):
    vectorizer = TfidfVectorizer(input=content, max_df=0.5, min_df=2, stop_words='english')
    X = vectorizer.fit_transform(content)

    km = KMeans(n_clusters=k, init='k-means++', max_iter=100)
    km.fit(X)

    order_centroids = km.cluster_centers_.argsort()[:, ::-1]
    terms = vectorizer.get_feature_names()

    clusters = dict()

    for i in range(k):
        topwords = []
        for ind in order_centroids[i, :20]:
            topwords.append(terms[ind])
        clusters[i+1] = topwords
    return clusters


if __name__ == '__main__':
    anansi = []
    with open("data/stream_wmata.json", 'r') as data_file:
        for line in data_file:
            tweet = json.loads(line)
            anansi.append((tweet['text']))

    results = clusterize(anansi, 10)
    for key, val in results.iteritems():
        print(key, val)
