import numpy as np
r=int(input('Rate:'))
p=int(input('Principle:'))
n=int(input('Months:'))
print(np.pmt(r,n,p))
