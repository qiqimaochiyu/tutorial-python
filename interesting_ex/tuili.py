#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 11:51:57 2018

@author: macbook
"""

from time import time
from constraint import Problem

problem = Problem()

# a1-a10 表示一到十题的答案，用1-4表示ABCD
vars = ['a1','a2','a3','a4','a5','a6','a7','a8','a9','a10']
problem.addVariables(vars, [1, 2, 3, 4])

#第二题
def a2_func(a2, a5):
    return (a2 == 1 and a5 == 3) or (a2 == 2 and a5 == 4) \
            or (a2 == 3 and a5 == 1) or (a2 == 4 and a5 == 2)
problem.addConstraint(a2_func, ['a2', 'a5'])

# 3
def a3_func(a3, a1, a2, a4, a6):
    return (a3 == 1 and a6 == a2 == a4 != a3) or (a3 == 2 and a3 == a2 == a4 != a6) \
        or (a3 == 3 and a3 == a6 == a4 != a2) or (a3 == 4 and a3 == a6 == a2 != a4)
problem.addConstraint(a3_func, ['a3', 'a1', 'a2', 'a4', 'a6'])

# 4
def a4_func(a4, a1, a2, a5, a6, a7, a9, a10):
    return (a4 == 1 and a1 == a5) or (a4 == 2 and a2 == a7) \
        or (a4 == 3 and a1 == a9) or (a4 == 4 and a6 == a10)
problem.addConstraint(a4_func, ['a4','a1','a2','a5','a6','a7','a9','a10'])

# 5
def a5_func(a4, a5, a7, a8, a9):
    return (a5 == a8 == 1) or (a5 == a4 == 2) or (a5 == a9 == 3) or (a5 == a7 == 4)
problem.addConstraint(a5_func, ['a4','a5','a7','a8','a9'])

# 6
def a6_func(a6, a1, a2, a3, a4, a5, a8, a9, a10):
    return (a6 == 1 and a2 == a4 == a8) or (a6 == 2 and a1 == a6 == a8) \
        or (a6 == 3 and a3 == a10 == a8) or (a6 == 4 and a5 == a9 == a8)
problem.addConstraint(a6_func, ['a6','a1','a2','a3','a4','a5','a8','a9','a10'])

# 7
def a7_func(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10):
    all_ans = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]
    count = [0, 0, 0, 0]
    for a in all_ans:
        count[a-1] += 1
    imin = count.index(min(count)) + 1
    return (a7 == 1 and imin == 3) or (a7 == 2 and imin == 2) \
        or (a7 == 3 and imin == 1) or (a7 == 4 and imin == 4)
problem.addConstraint(a7_func, vars)

# 8
def a8_func(a8, a1, a2, a5, a7, a10):
    adj = lambda x:abs(a1-x) != 1
    return (a8 == 1 and adj(a7)) or (a8 == 2 and adj(a5)) or (a8 == 3 and adj(a2)) \
        or (a8 == 4 and adj(a10))
problem.addConstraint(a8_func, ['a8','a1','a2','a5','a7','a10'])

# 9
def a9_func(a1, a2, a5, a6, a9, a10):
    cond1 = (a1 == a5)
    cond = lambda x:cond1 != (x == a5)
    return (a9 == 1 and cond(a6)) or (a9 == 2 and cond(a10)) \
        or (a9 == 3 and cond(a2)) or (a9 == 4 and cond(a9))
problem.addConstraint(a9_func, ['a1','a2','a5','a6','a9','a10'])

# 10
def a10_func(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10):
    all_ans = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]
    count = [0, 0, 0, 0]
    for a in all_ans:
        count[a-1] += 1
    delta = abs(max(count) - min(count))
    return (a10 == 1 and delta == 3) or (a10 == 2 and delta == 2) \
        or (a10 == 3 and delta == 4) or (a10 == 4 and delta == 1)
problem.addConstraint(a10_func, vars)


# 开始求解

start_time = time()
solutions = problem.getSolutions()
elapsed_time = time() - start_time
print('耗时:{0}'.format(elapsed_time))
print('可能的解数量:{0}'.format(len(solutions)))

chars = ['A', 'B', 'C', 'D']

for i in range(len(solutions)):
    print('\n-----{0}组解-----'.format(i+1))
    s = solutions[i]
    for j in range(1, 11):
        key = 'a' + str(j)
        answer = chars[s[key] - 1]
        print('第{0}题答案:{1}'.format(j, answer))
