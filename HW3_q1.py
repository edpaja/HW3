import numpy as np
import matplotlib
import matplotlib.pyplot as plt

year, spots = np.loadtxt("/Users/edouardsavalle/Desktop/University/grad/Computational_Physics/HW3/sunspots.txt", unpack=True)

fig, ax = plt.subplots(1, 1, figsize=(10, 5))
ax.plot(year, spots, "-")
ax.set(xlabel="months", xlim=(0, 3142), ylabel="Number of sunspots", title="Sunspot count since 1749")
ax.legend(fontsize=7)
ax.legend(); plt.tight_layout(); plt.savefig("sunspots.png", dpi=130); plt.close()