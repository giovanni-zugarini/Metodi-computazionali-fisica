import pandas as pd
import matplotlib.pyplot as plt

dati = pd.read_csv('E04/kplr010666592-2011240104155_slc.csv')
print(dati)

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