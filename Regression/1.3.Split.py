#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
from sklearn.model_selection import train_test_split

X, y = np.arange(10).reshape((5, 2)), range(5)
print('X=', X)
print("\n****************************************")

print('y=', list(y))
print("\n****************************************")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
print('X_train=' ,X_train)
print("\n****************************************")

print('y_train=',y_train)
print("\n****************************************")

print('X_test=' ,X_test)
print("\n****************************************")

print('y_test=', y_test)
