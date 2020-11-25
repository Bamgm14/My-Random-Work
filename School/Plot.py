import matplotlib.pyplot as plt
import math as m
import numpy as np
x=np.arange(0,4*np.pi,0.1)
y=np.sin(x)
z=np.cos(x)
m=np.tan(x)
def a(b):
    global x
    plt.plot(x,b)
    plt.show()
a(y)
a(z)
a(m)
