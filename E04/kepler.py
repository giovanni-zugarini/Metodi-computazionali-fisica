import pandas as pd
import matplotlib.pyplot as plt

dati = pd.read_csv('E04/kplr010666592-2011240104155_slc.csv')

print(dati.columns)

plt.figure(figsize=(10,5))
plt.plot(dati['TIME'], dati['PDCSAP_FLUX'])
plt.xlabel('Time (BJD)')
plt.ylabel('PDCSAP_FLUX (e-/s)')
plt.show()

plt.figure(figsize=(10,5))
plt.plot(dati['TIME'],dati['PDCSAP_FLUX'], 'o', markersize=2)
plt.xlabel('Time (BJD)')
plt.ylabel('PDCSAP_FLUX (e-/s)')
plt.show()

plt.figure(figsize=(10,5))
plt.errorbar(dati['TIME'], dati['PDCSAP_FLUX'], yerr=dati['PDCSAP_FLUX_ERR'], fmt='o', markersize=3)
plt.xlabel('Time (BJD)')
plt.ylabel('PDCSAP_FLUX (e-/s)')
plt.show()

plt.figure(figsize=(10,5))
tempo = dati.loc[(dati['TIME']<944) & (dati['TIME']>943.5)]
plt.errorbar(tempo['TIME'], tempo['PDCSAP_FLUX'], yerr=tempo['PDCSAP_FLUX_ERR'], fmt='o', markersize=3)
plt.xlabel('Time (BJD)')
plt.ylabel('PDCSAP_FLUX (e-/s)')
plt.savefig('grafico.png')
plt.show()

fig, ax =plt.subplots(figsize=(12,8))
ax.errorbar(dati['TIME'], dati['PDCSAP_FLUX'], yerr=dati['PDCSAP_FLUX_ERR'], color='tan', fmt='o', markersize=3)
ax.set_ylabel('FLUX (e-/s)')
ax.set_ylim(1.012e6, 1.032e6 )
ax.set_xlabel('Time (BJD)')
plt.grid()
ins_ax = ax.inset_axes([0.50, 0.65, 0.5, 0.3])
ins_ax.errorbar(tempo['TIME'], tempo['PDCSAP_FLUX'], yerr=tempo['PDCSAP_FLUX_ERR'], fmt='.')
plt.show()