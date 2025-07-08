# -*- coding: utf-8 -*-
"""
Created on Sun Jun  8 19:16:56 2025

@author: Pacific
"""

import keras as ks
from keras.models import Sequential
from keras.layers import Dense, Flatten
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error as mae
import matplotlib.pyplot as plt

data = np.load('/content/prepared dataset 5000 samples .npz')
X = data['matrix']
Y = data['mylist']