def euler(f, x0, y0, h, n):
    xs, ys = [], []
    for k in range(n):
        y0 += h * f(x0, y0)
        x0 += h
        print(f'x_{k+1}={x0}\ny_{k+1}={y0}\n')
        xs.append(x0)
        ys.append(y0)
    return xs, ys
    

if __name__ == '__main__':

   def f(x, y):
       return x + y

   x0 = 0 
   y0 = 0.5
   h = 0.2 
   n = 10  

xs, ys = euler(f, x0, y0, h, n)

import matplotlib.pyplot as plt
import numpy as np

def y(x):
  return 2 * np.exp(x) - x - 1

t = np.linspace(x0, x0 + n * h, 200)
yt = [y(ti) for ti in t]

plt.plot(t, yt)

plt.scatter(xs, ys)

plt.savefig("euler.png")
