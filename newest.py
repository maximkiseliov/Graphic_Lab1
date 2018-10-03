import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist import SubplotZero

x_val = []
y_val = []
y_built_in = []
abs_err = []

# my function of calculation
def my_func(x, eps):
    summ = 0
    k = 1
    term = 1

    while True:
        delta = (x - 1) / (k * x)
        term = term * delta
        summ += term
        k += 1

        if term <= eps:
            return summ

# run my_func for calculating
for x in np.linspace(1., 7., 19):
    x_val.append(round(x, 2))
    y_val.append(my_func(round(x, 2), 10 ** (-4)))

# creation of file 2    
res = {'x': x_val,
       'y': y_val}
file2 = open('file2.txt', 'w')
file2.close()
for i in range(len(res['x'])):
    file2 = open('file2.txt', 'a')
    reziki2 = "%s %s\n" % (str(res['x'][i]), str(res['y'][i]))
    file2.write(reziki2)
file2.close()

# run built-in function for calculating
for x in np.linspace(1., 7., 19):
    y_built_in.append(np.log(round(x, 2)))

#calculating absolute value of the difference of two functions
for i in range(len(y_val)):
    abs_err.append(abs(y_built_in[i] - y_val[i]))

# creation of file 1
res2 = {'x': x_val,
        'y_my_func': y_val,
        'y_built_in': y_built_in,
        'absolute_error': abs_err,
        'accuracy': 10 ** (-4)}
file1 = open('file1.txt', 'w')
file1.close()
for i in range(len(res2['x'])):
    file1 = open('file1.txt', 'a')
    reziki = "%s %s %s %s %s\n" % (str(res2['x'][i]), str(res2['y_my_func'][i]), str(res2['y_built_in'][i]), str(res2['absolute_error'][i]), str(res2['accuracy']))
    file1.write(reziki)
file1.close()
