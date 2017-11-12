#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 21:37:49 2017

@author: Juan
"""

import pandas as pd
import scipy
import sklearn

__author__ = "Juan"
__date__ = "$Nov 10, 2017 8:40:24 AM$"

r_cols=['user_id','movie_id','rating']
ratings=pd.read_csv('ml-latest/ratings.csv',names=r_cols,usecols=range(3))
ratings.head()
m_cols=['movie_id','title']
movies=pd.read_csv('ml-latest/movies.csv',names=m_cols,usecols=range(2))
movies.head()
ratings=pd.merge(movies,ratings)
ratings.head()
movieRatings=ratings.pivot_table(index=['user_id'],columns=['title'],values='rating',aggfunc = lambda x: x)
movieRatings.head()
starWarsRating= movieRatings["Round Midnight (1986)"]
starWarsRating.head()