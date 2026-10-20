import numpy as np
import matplotlib.pyplot as plt

blur = np.rot90(np.loadtxt("/Users/edouardsavalle/Desktop/University/grad/Computational_Physics/HW3/HW3_Q3/blur.txt", unpack=True))

fig, ax = plt.subplots(figsize=(7, 6))
im = ax.imshow(blur, origin="lower", cmap="seismic")   # try cmap="viridis" for color
fig.colorbar(im, ax=ax, label="Value")
ax.set(xlabel="x (pixel)", ylabel="y (pixel)", title="Image in blur.txt")
plt.tight_layout()
plt.savefig("/Users/edouardsavalle/Desktop/University/grad/Computational_Physics/HW3/HW3_Q3/composed_blur.png", dpi=130)
plt.show()