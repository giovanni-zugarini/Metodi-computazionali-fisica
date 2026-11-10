import numpy as np

def distanza(s,N,x0,y0):
    fi=np.random.uniform(0,2*np.pi,N)
    x=x0+s*np.cos(fi)
    y=y0+s*np.sin(fi)
    return np.array([x,y])
