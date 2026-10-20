import numpy as np
import scipy.fft
import matplotlib
import matplotlib.pyplot as plt

month, spots = np.loadtxt("/Users/edouardsavalle/Desktop/University/grad/Computational_Physics/HW3/sunspots.txt", unpack=True)

def dft(y):
    N = len(y)
    c = np.zeros(N//2+1, complex)
    for k in range(N//2+1): 
        for n in range(N):
            c[k]+=y[n]*np.exp(-2j*np.pi*k*n/N)
    return c

c = np.fft.fft(spots, n=3142)
print(c[0])
mag_c = abs(c**2)
print(mag_c[1:])
k = np.arange(0, 3142)



fig, ax = plt.subplots(1, 1, figsize=(10, 5))
ax.plot(k[1:], mag_c[1:], "-")
ax.set(xlabel="wavenumber, k/ t^-1", xlim=(20,30), ylabel="square of wavenumber coefficient, |c_k^2|", title="Power spectrum of sunspot data since 1749")
ax.legend(fontsize=7)
ax.legend(); plt.tight_layout(); plt.savefig("sunspots_power_spectrum_implemented.png", dpi=130); plt.close()