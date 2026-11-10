import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return (3/1000)*(x**2)

N=100000
x_min=0.00
y_min=0.00
x_max=10
y_max=f(x_max)

x=np.random.uniform(x_min, x_max, N)
y=np.random.uniform(y_min, y_max, N)
mask=y <=f(x)
x_acc=x[mask]
y_acc=y[mask]
plt.figure(figsize=(12,8))
plt.hist(x_acc, bins=50,range=(x_min,x_max), alpha=0.6, density=True, edgecolor='black', label='Campioni accettati')
plt.xlabel("X")
plt.ylabel('densità di probabilità')


xv=np.linspace(x_min,x_max,500)
plt.plot(xv,f(xv),color='r',label=r'teorica: $f(x)=3/1000 x^2$')
plt.legend()
plt.title('Metodo Hit/Miss')
plt.grid(True, alpha=0.5)
plt.show()

z=np.random.uniform(0.0,10.0,N)
x_cum=x_max*(z**(1/3))
plt.figure(figsize=(12,8))
plt.hist(x_cum, bins=50,range=(x_min,x_max), alpha=0.6, density=True, edgecolor='black',label='Campioni accettati')
xv=np.linspace(x_min,x_max,500)
plt.plot(xv,f(xv),color='r',label=r'teorica: $f(x)=3/1000 x^2$')
plt.title('Metodo cumulativo')
plt.xlabel('X conteggiate')
plt.ylabel('densità di probabilità')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()