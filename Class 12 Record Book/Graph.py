import numpy as np
from matplotlib import pyplot as plt
x=np.arange(-100,100)
y=x**2
plt.plot(x,y)
plt.savefig('Graph.png')
