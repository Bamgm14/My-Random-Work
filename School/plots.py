import matplotlib.pyplot as plt
import numpy as np

fs = 100
f = 2

x = np.arange(fs)
y = [ np.sin(2*np.pi*f * (i/fs)) for i in x]
plt.stem(x,y, 'r', )
plt.plot(x,y)
