import numpy as np

def distanza(s,N,x0,y0):
    fi=np.random.uniform(0,2*np.pi,N)
    dx=x0+s*np.cos(fi)
    dy=y0+s*np.sin(fi)
    x=np.cumsum(np.insert(dx,x0,y0))
    y=np.cumsum(np.insert(dy,x0,y0))
    return np.array([x,y])
