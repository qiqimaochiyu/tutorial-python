#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 19:33:34 2017

@author: macbook_wy
"""

import urllib
import numpy 
from sklearn import datasets,linear_model
from sklearn.linear_model import LassoCV
from math import sqrt
import matplotlib.pyplot as plot

target_url = ("http://archive.ics.uci.edu/ml/machine-learning-"
              "databases/wine-quality/winequality-red.csv")
data = urllib.request.urlopen(target_url)
# data = data.read()
xList = []
labels = []
names = []
firstLine = True

for line in data:
    line = line.decode()
    if firstLine:
        names = line.strip().split(";")
        firstLine = False
    else:
        row = line.strip().split(";")
        labels.append(float(row[-1]))
        row.pop()
        floatRow = [float(num) for num in row]
        xList.append(floatRow)

nrows = len(xList)
ncols = len(xList[0])

xMeans = []
xSD = []       
for i in range(ncols):
    col = [xList[j][i] for j in range(nrows)]
    mean = sum(col)/nrows
    xMeans.append(mean)
    colDiff = [(xList[j][i] - mean) for j in range(nrows)]
    sumSq = sum([colDiff[i] * colDiff[i] for i in range(nrows)])
    stdDev = sqrt(sumSq/nrows)
    xSD.append(stdDev)

xNormalized = []
for i in range(nrows):
    rowNormalized = [(xList[i][j] - xMeans[j])/xSD[j] for j in range(ncols)]
    xNormalized.append(rowNormalized)
    
meanLabel = sum(labels)/nrows

sdLabel = sqrt(sum([(labels[i]-meanLabel)**2 for i in range(nrows)])/nrows)

labelNormalized = [(labels[i] - meanLabel)/sdLabel for i in range(nrows)]

Y = numpy.array(labels)

#Y = numpy.array(labelNormalized)

#X = numpy.array(xList)

X = numpy.array(xNormalized)

wineModel = LassoCV(cv=10).fit(X,Y)

plot.figure
plot.plot(wineModel.alphas_, wineModel.mse_path_, ':')
plot.plot(wineModel.alphas_, wineModel.mse_path_.mean(axis=-1),label='Average MSE Across Folds',linewidth=2)
plot.axvline(wineModel.alpha_, linestyle='--',label='CV Estimate of Best alpha')
plot.semilogx()
plot.legend()
ax = plot.gca()
ax.invert_xaxis()
plot.xlabel('alpha')
plot.ylabel('Mean Square Error')
plot.axis('tight')
plot.show()

print("alpha value that min cv error ", wineModel.alpha_)
print("min mse", min(wineModel.mse_path_.mean(axis=-1)))







