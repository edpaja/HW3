import numpy as np
import matplotlib.pyplot as plt

blur = np.rot90(np.loadtxt("/Users/edouardsavalle/Desktop/University/grad/Computational_Physics/HW3/HW3_Q3/blur.txt", unpack=True))
spread = np.zeros_like(blur)

N = blur.shape[0]
eps = 10**(-3)
sigma = 10

idx = np.arange(N)
d = np.where(idx < N // 2, idx, idx - N)

X, Y = np.meshgrid(d, d)
spread = np.exp(-(X**2 + Y**2) / (2 * sigma**2))

b_squig = np.fft.rfft2(blur)
f_squig = np.fft.rfft2(spread)
a_squig = np.zeros_like(f_squig)
for x in range(f_squig.shape[0]):
    for y in range(f_squig.shape[1]):
        if np.abs(f_squig[x, y]) < eps:
            a_squig[x, y] = b_squig[x, y] / N**2
        else:
            a_squig[x, y] = b_squig[x, y] / (N**2 * f_squig[x, y])

print(a_squig)
a = np.fft.irfft2(a_squig)
print(a)

fig, ax = plt.subplots(figsize=(7, 6))
im = ax.imshow(a, origin="lower", cmap="seismic")
fig.colorbar(im, ax=ax, label="Value")
ax.set(xlabel="x (pixel)", ylabel="y (pixel)", title="Deconvoluted Image with Epsilon=10^-3, sigma = 20")
plt.tight_layout()
plt.savefig("/Users/edouardsavalle/Desktop/University/grad/Computational_Physics/HW3/HW3_Q3/neat_seismic_10-3.png", dpi=130)
plt.show()

