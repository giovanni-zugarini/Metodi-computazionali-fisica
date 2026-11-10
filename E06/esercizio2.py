import cammino
import numpy as np
import matplotlib.pyplot as plt

l_s=[1,0.5,2,3.5,1.5]
N=10000
plt.figure(figsize=(12,8))
for i in range(len(l_s)):
    
    plt.plot(cammino.distanza(l_s[i],N,0,0)[0], cammino.distanza(l_s[i],N,0,0)[1], alpha=0.8, label=f"walker {i+1}")

plt.xlabel('posizione x')
plt.ylabel('posizione y')
plt.legend()
plt.grid(True, alpha=0.7)
plt.show()