#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 15:16:15 2018

@author: AliBaba
"""

#choices = [1,1,3,5,3]
#total = 5
import numpy as np
def find_combination(choices, total):
    temp, ya, ref = 0, [], {}
    if len(set(choices)) < len(choices):
        for x in choices:
            if x + temp <= total:
                temp += x 
                ya.append(1)
            else:
                ya.append(0)
        return np.array(ya) 
    else:
        meow = sorted(choices, reverse=True)
        for x in meow:
            if x + temp <= total:
                temp += x
                ref[x] = 1
            else:
                ref[x] = 0
        for n in choices:
            ya.append(ref[n])
        return np.array(ya)



# =============================================================================
#     temp, ya = 0, []
#     for x in choices:
#         if x + temp <= total:
#             temp += x
#             ya.append(1)
#         else:
#             ya.append(0)
#     return np.array(ya)
# =============================================================================
