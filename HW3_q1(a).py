import numpy as np
import scipy.fft
import matplotlib
import matplotlib.pyplot as plt

month, spots = np.loadtxt("/Users/edouardsavalle/Desktop/University/grad/Computational_Physics/HW3/sunspots.txt", unpack=True)

fig, ax = plt.subplots(1, 1, figsize=(10, 5))
ax.plot(month, spots, "-")
ax.set(xlabel="Months since 1749", xlim=(0,100), ylabel="Number of sunspots", title="Sunspot frequency since 1749")
ax.legend(fontsize=7)
ax.legend(); plt.tight_layout(); plt.savefig("sunspots.png", dpi=130); plt.close()