#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 2*x**2+1

a=0 #Starting point of integration.
b=10 #end point of integration.
h=10 #number of steps

x=np.linspace(a,b,h)
y=f(x)

def integ(y,a,b,h):
    dx=(b-a)/h
    return dx*sum(y)

result=integ(y,a,b,h)
print(result)

x_rect=x[1:] #To construct our rectangles
y_rect=y[1:]
dx=(b-a)/h
 

plt.plot(x,y)
plt.bar(x_rect,y_rect,dx,alpha=.4,color='orange',edgecolor='black',align='edge')
plt.grid()
plt.show()
