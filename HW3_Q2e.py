import numpy as np
import matplotlib.pyplot as plt
import numpy.fft as fft

dcv = np.loadtxt("/Users/edouardsavalle/Desktop/University/grad/Computational_Physics/HW3/HW3_Q2/dow.txt", unpack=True)

c_k = fft.rfft(dcv)
print(len(c_k))
cutoff_10 = int(len(c_k)//10)
c_seg_10 = np.concatenate((c_k[0:cutoff_10], np.zeros(len(c_k)-cutoff_10)))
dcv_seg_10 = fft.irfft(c_seg_10)
cutoff_2 = int(len(c_k)//50)
c_seg_2 = np.concatenate((c_k[0:cutoff_2], np.zeros(len(c_k)-cutoff_2)))
dcv_seg_2 = fft.irfft(c_seg_2)
k = np.arange(0, len(c_k))
day = np.arange(1, len(dcv)+1)

fig, ax = plt.subplots(1, 1, figsize=(10, 5))
ax.plot(day, dcv, color="green", linestyle="-", label="Full data")
ax.plot(day, dcv_seg_10, color="blue", linestyle="-", label="First 10% of harmonics")
ax.plot(day, dcv_seg_2, color="red", linestyle="-", label="First 2% of harmonics")
ax.set(xlabel="days", xlim=(0, len(day)), ylabel="Daily Closing Value/$",
       title="'Smoothed' graph of the Dow Daily Closing Value")
ax.legend(loc="best")
plt.tight_layout()
plt.savefig("/Users/edouardsavalle/Desktop/University/grad/Computational_Physics/HW3/HW3_Q2/dow_inverserfft.png", dpi=130)
plt.close()
