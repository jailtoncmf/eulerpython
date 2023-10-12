def euler(f, x0, y0, h, n):
   
    for k in range(n):
        y0 += h * f(x0, y0)
        x0 += h
        print(f'x_{k+1}={x0}\ny_{k+1}={y0}\n')

    

if __name__ == '__main__':

  def f(x, y):
    return x + y

x0 = 0 
y0 = 0.5
h = 0.2 
n = 10  

euler(f, x0, y0, h, n)
