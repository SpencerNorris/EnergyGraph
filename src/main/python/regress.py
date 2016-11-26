#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import statsmodels.api as sm
import numpy as np

#Derived from http://statsmodels.sourceforge.net/stable/

# check the p_value
def reg_m(y, x):
    ones = np.ones(len(x[0]))
    # check to make sure a constant is not already included
    X = sm.add_constant(np.column_stack((x[0], ones)))
    for ele in x[1:]:
        X = sm.add_constant(np.column_stack((ele, X)))
    results = sm.OLS(y, X).fit()
    return results

# print reg_m(diabetes_y_train, diabetes_X_train),summary()
y = [1,2,3,4,3,4,5,4,5,5,4,5,4,5,4,5,6,5,4,5,4,3,4]

x = [
     [4,2,3,4,5,4,5,6,7,4,8,9,8,8,6,6,5,5,5,5,5,5,5],
     [4,1,2,3,4,5,6,7,5,8,7,8,7,8,7,8,7,7,7,7,7,6,5],
     [4,1,2,5,6,7,8,9,7,8,7,8,7,7,7,7,7,7,6,6,4,4,4],
     [2,3,5,7,8,9,1,4,5,2,3,6,7,8,9,4,3,7,2,1,5,6,4]
     ]

print reg_m(y, x).summary()
