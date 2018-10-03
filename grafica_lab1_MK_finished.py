import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist import SubplotZero

accuracy = 10 ** (-4)
x_arg = []
y_myfunc = []
y_built_in = []
abs_err = []

# my function of calculation
def my_func(x, eps):
    summ = 0
    k = 1
    term = 1

    while True:
        delta = (x - 1) / x
        term = term * delta
        summ += term / k
        k += 1

        if term <= eps:
            return summ


# run my_func for calculating
for x in np.linspace(0.65, 15., 39):
    x_arg.append(round(x, 2))
    y_myfunc.append(my_func(round(x, 2), accuracy)) # run my_func for calculating
    y_built_in.append(np.log(round(x, 2))) # run built-in function for calculating


#calculating absolute value of the difference of two functions
for i in range(len(y_myfunc)):
    abs_err.append(abs(y_built_in[i] - y_myfunc[i]))


# creation of file 1
res2 = {'x': x_arg,
        'y_my_func': y_myfunc,
        'y_built_in': y_built_in,
        'absolute_error': abs_err,
        'accuracy': accuracy}
file1 = open('file1.txt', 'w')
file1.close()
for i in range(len(res2['x'])):
    file1 = open('file1.txt', 'a')
    reziki = "%s %s %s %s %s\n" % (str(res2['x'][i]), str(res2['y_my_func'][i]), str(res2['y_built_in'][i]), str(res2['absolute_error'][i]), str(res2['accuracy']))
    file1.write(reziki)
file1.close()


# creation of file 2    
res = {'x': x_arg,
       'y': y_myfunc}
file2 = open('file2.txt', 'w')
file2.close()
for i in range(len(res['x'])):
    file2 = open('file2.txt', 'a')
    reziki2 = "%s %s\n" % (str(res['x'][i]), str(res['y'][i]))
    file2.write(reziki2)
file2.close()


#building graph
fig = plt.figure(1)
ax = SubplotZero(fig, 111)
fig.add_subplot(ax)

for direction in ["xzero", "yzero"]:
    ax.axis[direction].set_axisline_style("-|>")
    ax.axis[direction].set_visible(True)

for direction in ["left", "right", "bottom", "top"]:
    ax.axis[direction].set_visible(False)

ax.plot(res['x'], res['y'], 'g', label = 'my function')
ax.scatter(res2['x'], res2['y_built_in'],color='red', label = 'built-in function')
plt.legend(loc='lower right')
plt.show()
