#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 00:14:32 2023

@author: johnpaulmbagwu
"""
# Python code for 2D random walk. 
import sys
import numpy
import matplotlib.pyplot as plt
import pylab 
import random
import math
import random 
sys.path.append(".")
import Random as rng

# default seed
seed = 5556

# class instance of our Random class using seed
random = rng.Random(seed)

# defining the number of steps 
Nstep = 300
# number of walks
Nwalk = 2000
#############################################################
################"FAIR" RANDOM WALK #######################
#############################################################
# Define positions and displacement in arrays
x = numpy.zeros(Nstep) 
y = numpy.zeros(Nstep)
xfinal = []
yfinal = []
finald = []
# filling the coordinates with Categorical numbers
for j in range(1,Nwalk+1):
    for i in range(1, Nstep):
        val = random.Categorical(0.35,0.35,0.35,0.35,0.35,0.35) 
        if val == 1: 
            x[i] = x[i - 1] + 1
            y[i] = y[i - 1] 
        elif val == 2: 
            x[i] = x[i - 1] - 1
            y[i] = y[i - 1] 
        elif val == 3: 
            x[i] = x[i - 1] 
            y[i] = y[i - 1] + 1
        elif val == 4: 
            x[i] = x[i - 1] 
            y[i] = y[i - 1] + 1
        elif val == 5: 
            x[i] = x[i - 1] 
            y[i] = y[i - 1] + 1
        elif val == 6: 
            x[i] = x[i - 1] 
            y[i] = y[i - 1] + 1
        else: 
            x[i] = x[i - 1] 
            y[i] = y[i - 1] - 1
    finald.append(numpy.sqrt(x[Nstep-1]*x[Nstep-1]+y[Nstep-1]*y[Nstep-1]))
    xfinal.append(x[Nstep-1])
    yfinal.append(y[Nstep-1])
#############################################################
################"BIASED" RANDOM WALK #######################
#############################################################

# Define positions and displacement in arrays
xbias = numpy.zeros(Nstep) 
ybias = numpy.zeros(Nstep)
xfinalbias = []
yfinalbias = []
finaldbias = []

# filling the coordinates with Categorical numbers with
# probabilities coming from an exponential distribution
for j in range(1,Nwalk+1):
    for i in range(1, Nstep):
        val = random.Categorical(random.TruncExp(1., 0., 1.),random.TruncExp(1., 0., 1.),random.TruncExp(1., 0., 1.)) 
        if val == 1: 
            xbias[i] = xbias[i - 1] + 1
            ybias[i] = ybias[i - 1] 
        elif val == 2: 
            xbias[i] = xbias[i - 1] - 1
            ybias[i] = ybias[i - 1] 
        elif val == 3: 
            xbias[i] = xbias[i - 1] 
            ybias[i] = ybias[i - 1] + 1
        elif val == 4: 
            xbias[i] = xbias[i - 1] 
            ybias[i] = ybias[i - 1] + 1
        elif val == 5: 
            xbias[i] = xbias[i - 1] 
            ybias[i] = ybias[i - 1] + 1
        elif val == 6: 
            xbias[i] = xbias[i - 1] 
            ybias[i] = ybias[i - 1] + 1
        else: 
            xbias[i] = xbias[i - 1] 
            ybias[i] = ybias[i - 1] - 1
    finaldbias.append(numpy.sqrt(xbias[Nstep-1]*xbias[Nstep-1]+ybias[Nstep-1]*ybias[Nstep-1]))
    xfinalbias.append(xbias[Nstep-1])
    yfinalbias.append(ybias[Nstep-1])
################################################################
###############"FAIR" RANDOM WALK PLOTS#########################
################################################################
plt.plot(xfinal, yfinal, 'p', color='red')
plt.grid(axis='x', alpha=0.75)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Final positions after ' + str(Nwalk) + ' random walks')
plt.show()
f1 = numpy.linspace(0.0,25.0,1000)
f2 = 2*f1/Nstep * numpy.exp(-f1*f1/Nstep)
plt.plot(f1,f2, color='black', linestyle='dashed', label = 'Rayleigh distribution, N= ' + str(Nstep))
n, bins, patches = plt.hist(finald, 15 , density = True, color ='yellow', alpha=0.6, fill = True, hatch='/',histtype='step', linewidth=1, label = 'data')
plt.legend(loc='upper right')
plt.title('Data distribution in comparison to the Rayleigh distribution ')
plt.xlabel('r')
plt.ylabel('Probability')
plt.grid(axis='y', alpha=0.75)
plt.show()
################################################################
###############"BIASED" RANDOM WALK PLOTS#########################
################################################################
plt.plot(xfinalbias, yfinalbias, 'p', color='red')
plt.grid(axis='x', alpha=0.75)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Final positions after ' + str(Nwalk) + ' random walks')
plt.show()
#f1 = numpy.linspace(0.0,25.0,1000)
#f2 = 2*f1/float(n) * numpy.exp(-f1*f1/float(n))
plt.plot(f1,f2, color='black', linestyle='dashed', label = 'Rayleigh distribution, N= ' + str(Nstep))
n, bins, patches = plt.hist(finaldbias, 15 , density = True, color ='green', alpha=0.6, fill = True, hatch='/',histtype='step', linewidth=1, label = 'data')
plt.legend(loc='upper right')
plt.title('Data distribution in comparison to the Rayleigh distribution ')
plt.xlabel('r')
plt.ylabel('Probability')
plt.grid(axis='y', alpha=0.75)
plt.show()
