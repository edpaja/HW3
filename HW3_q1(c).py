import numpy as np
import scipy.fft
import matplotlib
import matplotlib.pyplot as plt

month, spots = np.loadtxt("/Users/edouardsavalle/Desktop/University/grad/Computational_Physics/HW3/sunspots.txt", unpack=True)
k_max = 24
c_0 = 163177.1/3142
N = len(month)
y = c_0 + c_0*np.sin(2*np.pi*(k_max/N)*month)
print(y)

fig, ax = plt.subplots(1, 1, figsize=(10, 5))
ax.plot(month, spots, "-")
ax.plot(month, y)
ax.set(xlabel="Months since 1749", xlim=(0,3142), ylabel="Number of sunspots", title="Sunspot frequency since 1749")
ax.legend(fontsize=7)
ax.legend(); plt.tight_layout(); plt.savefig("sunspots_sin.png", dpi=130); plt.close()