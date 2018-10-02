import math
from numpy import linspace
from tkinter import *
import matplotlib.pyplot as plt

accur = 10 ** (-4)
x_val = []
y_val = []
y_built_in = []
abs_err = []

x0 = 40
y0 = 240
xm = 480
ym = 20

# my function of calculation
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

# function to create Graph of a function
def coord(x0, y0, xm, ym, fil_color):
    canv.create_line(x0-10, y0, xm+10, y0, fill=fil_color, arrow=LAST)
    canv.create_line(x0, ym-10, x0, 2*y0-ym+10, fill=fil_color, arrow=FIRST)

# function to create lines
def figure(dictionary, x0, y0, fil_color):
    xb = x0 + dictionary['x'][0]
    yb = y0 + dictionary['y'][0]
    
    canv.create_line(xb, yb, xb, yb, fill=fil_color)

    for i in range(1, len(dictionary['x'])):
        x = x0 + dictionary['x'][i]
        y = y0 + dictionary['y'][i]
        
        canv.create_line(xb, yb, x, y, fill=fil_color)
        #canv.create_oval(xb, yb, xb, yb, width = 0, fill = 'red')
        xb = x
        yb = y

# run my_func for calculating
for x in linspace(5, 15, 28):
    x_val.append(round(x, 2))
    y_val.append(my_func(round(x, 2), accur))

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
for x in linspace(5, 15, 28):
    y_built_in.append(math.log(x))

#calculating absolute value of the difference of two functions
for i in range(len(y_val)):
    abs_err.append(abs(y_built_in[i] - y_val[i]))

# creation of file 1
res2 = {'x': x_val,
        'y_my_func': y_val,
        'y_built_in': y_built_in,
        'absolute_error': abs_err,
        'accuracy': accur}
file1 = open('file1.txt', 'w')
file1.close()
for i in range(len(res2['x'])):
    file1 = open('file1.txt', 'a')
    reziki = "%s %s %s %s %s\n" % (str(res2['x'][i]), str(res2['y_my_func'][i]), str(res2['y_built_in'][i]), str(res2['absolute_error'][i]), str(res2['accuracy']))
    file1.write(reziki)
file1.close()


root = Tk()
canv = Canvas(root, width=500, height=500)
canv.pack()
coord(x0, y0, xm, ym, 'blue')
figure(res, x0, y0, 'red')
root.mainloop()

'''
plt.scatter(res['x'], y_built_in)
plt.plot(res['x'], res['y'])
plt.show()
'''
