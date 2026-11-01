import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dati = pd.read_csv('ExoplanetsPars_2025.csv', comment='#')
print(dati.columns)

dati.head(10)

plt.figure(figsize=(12,8))
plt.scatter(dati['pl_orbper'],dati['pl_bmassj'],s=9, color='darkorchid')
plt.title('Massa del pianeta in funzione del periodo orbitale')
plt.xlabel('periodo orbitale (giorni)')
plt.ylabel('Massa del pianeta (masse di giove)')
plt.xscale('log')
plt.yscale('log')
plt.show()

plt.figure(figsize=(12,8))
plt.scatter(dati['pl_orbper'],(dati['pl_orbsmax']**2)/dati['st_mass'],s=9, color='darkgoldenrod')
plt.title(r'rapporto $R_{\text{max}}^2 / m_*$ in funzione del periodo orbitale')
plt.xlabel('Periodo orbitale (giorni)')
plt.ylabel(r'$R_{\text{max}}^2/m_*$ ($m^2$/days)')
plt.xscale('log')
plt.yscale('log')
plt.show()

plt.figure(figsize=(12,8))
datirv = dati.loc[dati['discoverymethod'] == 'Radial Velocity']
datitr = dati.loc[dati['discoverymethod'] == 'Transit']
plt.scatter(datirv['pl_orbper'], datirv['pl_bmassj'], s=6, alpha=0.5)
plt.scatter(datitr['pl_orbper'], datitr['pl_bmassj'], s=6, alpha=0.5)
plt.xlabel('periodo orbitale(giorni)')
plt.ylabel('massa del pianeta')
plt.xscale('log')
plt.yscale('log')
plt.title('massa del pianeta in funzione del periodo orbitale per metodo di scoperta')
plt.show()

plt.figure(figsize=(12,8))
xmin = min(datirv['pl_bmassj'].min(), datitr['pl_bmassj'].min())
xmax = max(datirv['pl_bmassj'].max(), datitr['pl_bmassj'].max())
plt.hist(datirv['pl_bmassj'], bins=30, range=(xmin,xmax), alpha=0.5, label='Radial Velocity')
plt.hist(datitr['pl_bmassj'], bins=30, range=(xmin,xmax), alpha=0.5, label='Tranist')
plt.xlabel('massa pianeta')
plt.ylabel('conteggio')
plt.title('distribuzione massa degli esopianeti per metodo di scoperta')
plt.legend()
plt.show()

logrv = np.log10(datirv['pl_bmassj'])
logtr = np.log10(datitr['pl_bmassj'])
xminlog = min(logrv.min(),logtr.min())
xmaxlog = max(logrv.max(),logtr.max())
plt.figure(figsize=(12,8))
plt.hist(logrv, bins=30, range=(xminlog,xmaxlog), alpha=0.5, label='Radial Velocity')
plt.hist(logtr, bins=30, range=(xminlog,xmaxlog), alpha=0.5, label='Transit')
plt.xlabel(r'$\log_{10}(\text{massa})$')
plt.ylabel('conteggio')
plt.title(r'distribuzione $\log_{10}(\text{massa})$ per metodo di scoperta')
plt.legend()
plt.show()