import numpy as np

def somma_n(n):
    somma = 0
    for i in range(n+1):
        somma = somma +i
    print(somma)

def somma_prodotto(n):
    somma = 0
    prodotto = 1
    for i in range(n+1):
        if i == 0:
            somma = somma
            prodotto = prodotto
        else:
            somma = somma + i
            prodotto = prodotto * i
    print(somma)
    print(prodotto)

def sommatoria(n, a=1):
   print(np.sum(np.arange(n+1)**a))
   return