#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 15:10:53 2018

@author: AliBaba
"""

import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP
    pRabr = 1 - (CURRENTRABBITPOP/MAXRABBITPOP)
    if random.random() < pRabr:
        CURRENTRABBITPOP += 1
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    if CURRENTRABBITPOP > 10:
        pFoxr = CURRENTRABBITPOP/MAXRABBITPOP
        if random.random() < pFoxr:
            CURRENTRABBITPOP -= 1
            if random.random() < (1/3):
                CURRENTFOXPOP += 1
        else:
            if CURRENTFOXPOP > 10:
                if random.random() < 0.9:
                    CURRENTFOXPOP -= 1
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    rabbit_populations, fox_populations = [], []
    for x in range(numSteps):
        for r in range(CURRENTRABBITPOP):
            rabbitGrowth()
        for f in range(CURRENTFOXPOP):
            foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)
    return (rabbit_populations, fox_populations)

def plot(steps):
    z = runSimulation(steps)
    pylab.plot(range(steps), z[0], label = 'Rabbits')
    pylab.plot(range(steps), z[1], label = 'Foxes')
    pylab.xlabel('Time Steps')
    pylab.ylabel('Population')
    Rcoef = pylab.polyfit(range(steps), z[0], 2)
    pylab.plot(range(steps), pylab.polyval(Rcoef, range(steps)), label = 'Rabz')
    Fcoef = pylab.polyfit(range(steps), z[1], 2)
    pylab.plot(range(steps), pylab.polyval(Fcoef, range(steps)), label = 'Foxez')
    pylab.legend()