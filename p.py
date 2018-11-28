import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def funcion(x):
    return x**2.0

def integrar(x,h,N):
    w=np.ones(N)*h
    f=funcion(x)
    return np.sum(np.multiply(w,f))

N=100
x1=np.linspace(-1,1,N)
h1=(x1[-1]-x1[0])/N

print (integrar(x1,h1,N))

#########

def s(x):
    return np.sin(x)

def derivar(x,h):
    return (s(x[1:])-s(x[:-1]))/h

x2=np.linspace(-np.pi,np.pi,N)
h2=(x2[-1]-x2[0])/N

ys=s(x2)
yc=derivar(x2,h2)

g=plt.figure(1)
plt.plot(x2,ys)
plt.plot(x2[:-1],yc)
g.savefig('pr.pdf')