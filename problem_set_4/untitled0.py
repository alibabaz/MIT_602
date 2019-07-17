#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 17:44:46 2018

@author: AliBaba
"""

import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    B = ['G', 'G', 'G', 'R', 'R', 'R']
    sux = 0
    for x in range(numTrials):
        pull = []
        for i in range(3):
            pull.append(B[random.randint(0, (5-i))])
        if len(set(pull)) == 1:
            sux += 1
    return(sux/numTrials)