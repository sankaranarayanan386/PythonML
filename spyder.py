# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 12:27:45 2018

@author: 668376
"""

import pandas as pd
movies = pd.read_csv('movies.csv', sep=',')
rating=pd.read_csv('rating1.csv',sep=',')
tags = pd.read_csv('tags.csv', sep=',')
links=pd.read_csv('links.csv',sep=',')
joined=pd.concat([movies,rating],keys = 'movieId').groupby(movies['movieId'])
print(joined.head())