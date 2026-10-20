import numpy as np
import matplotlib.pyplot as plt

blur = np.rot90(np.loadtxt("/Users/edouardsavalle/Desktop/University/grad/Computational_Physics/HW3/HW3_Q3/blur.txt", unpack=True))
spread = np.zeros_like(blur)

N = blur.shape[0]
eps = 10**(-3)
sigma = 25

idx = np.arange(N)
d = np.where(idx < N // 2, idx, idx - N)

X, Y = np.meshgrid(d, d)
spread = np.exp(-(X**2 + Y**2) / (2 * sigma**2))

fig, ax = plt.subplots(figsize=(7, 6))
im = ax.imshow(spread, origin="lower", cmap="seismic")
fig.colorbar(im, ax=ax, label="Value")
ax.set(xlabel="x (pixel)", ylabel="y (pixel)", title="Gaussian spread")
plt.tight_layout()
plt.savefig("/Users/edouardsavalle/Desktop/University/grad/Computational_Physics/HW3/HW3_Q3/spread_seismic.png", dpi=130)
plt.show()