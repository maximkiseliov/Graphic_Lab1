import math
from numpy import linspace
from tkinter import *
import matplotlib.pyplot as plt

accur = 10 ** (-4)

def my_func(x, eps):
    summ = 0
    k = 1
    term = 0

    while True:
        term = (((x-1)**k)/ (k*(x**k)))
        #delta = (x - 1) / (k * x)
        #term = term * delta
        summ += term
        k += 1

        if term <= eps:
            return summ

x_val = []
y_val = []

for x in linspace(0.5, 15, 30):
    x_val.append(round(x, 2))
    y_val.append(my_func(round(x, 2), accur))

res = {'x': x_val,
       'y': y_val}

y_built_in = []
for x in linspace(0.5, 15, 30):
    y_built_in.append(math.log(x))

abs_err = []
for i in range(len(y_val)):
    abs_err.append(abs(y_built_in[i] - y_val[i]))

res2 = {'x': x_val,
        'y_my_func': y_val,
        'y_built_in': y_built_in,
        'absolute_error': abs_err,
        'accuracy': accur}

for i in range(len(res2['x'])):
    file1 = open('file1.txt', 'a')
    reziki = "%s %s %s %s %s\n" % (str(res2['x'][i]), str(res2['y_my_func'][i]), str(res2['y_built_in'][i]), str(res2['absolute_error'][i]), str(res2['accuracy']))
    file1.write(reziki)
file1.close()

for i in range(len(res['x'])):
    file2 = open('file2.txt', 'a')
    reziki2 = "%s %s\n" % (str(res['x'][i]), str(res['y'][i]))
    file2.write(reziki2)
file2.close()

plt.scatter(res['x'], y_built_in)
plt.plot(res['x'], res['y'])
plt.show()
