import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dati = pd.read_csv('ExoplanetsPars_2025.csv', comment='#')
print(dati.columns)

dati.head(10)

plt.figure(figsize=(12,8))
plt.scatter(dati['pl_orbper'],dati['pl_bmassj'],s=9, color='darkorchid')
plt.xlabel('Tempo (giorni)')
plt.ylabel('Massa (masse di giove)')
plt.xscale('log')
plt.yscale('log')
plt.show()

plt.figure(figsize=(12,8))
plt.scatter(dati['pl_orbper'],(dati['pl_orbsmax']**2)/dati['st_mass'],s=9, color='darkgoldenrod')
plt.xlabel('Tempo (giorni)')
plt.ylabel('$R_{max}^2/m_{*}$ ($m^2$/days)')
plt.xscale('log')
plt.yscale('log')
plt.show()

plt.figure(figsize=(12,8))
datirv = dati.loc[dati['discoverymethod'] == 'Radial Velocity']
datitr = dati.loc[dati['discoverymethod'] == 'Transit']
plt.scatter(datirv['pl_orbper'], datirv['pl_bmassj'], s=6, alpha=0.5)
plt.scatter(datitr['pl_orbper'], datitr['pl_bmassj'], s=6, alpha=0.5)
plt.xlabel('Tempo (giorni)')
plt.ylabel('')
plt.xscale('log')
plt.yscale('log')
plt.show()