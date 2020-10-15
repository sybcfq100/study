import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

data = np.loadtxt('/Users/sybcf/Documents/work/123.txt')
f = data[:, 0][0:1001]
r_all = data[:, 1]
arr = r_all.reshape(r_all.shape[0], 1)
arrT = arr.reshape(4, 1001)
r_T = arrT.T
f_r = np.c_[f, r_T]
np.savetxt('f_r.txt', f_r)

font1 = {'family': 'Times New Roman', 'weight': 'normal', 'size': 12, }

font2 = {'family': 'Times New Roman', 'weight': 'normal', 'size': 14, }

figsize = 7, 5
figure, ax = plt.subplots(figsize=figsize)
plt.title('On/Off state with(/out) loss', font2)

plt.plot(f_r[:, 0], f_r[:, 1], color='black', linewidth='2', label='R = 6; w/loss')
plt.plot(f_r[:, 0], f_r[:, 2], color='gray', linewidth='1', linestyle='-.', marker='+', label='R = 6; o/loss')
plt.plot(f_r[:, 0], f_r[:, 3], color='red', linewidth='2', label='R = 1500; w/loss')
plt.plot(f_r[:, 0], f_r[:, 4], color='pink', linewidth='1', linestyle='-.', marker='+', label='R = 1500; o/loss')
plt.legend(prop=font1)
plt.tick_params(labelsize=12)
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]

plt.xlabel('Frequency (GHz)', font2)
plt.ylabel('S11 (linear)', font2)

ax.yaxis.set_major_locator(MultipleLocator(0.1))
ax.xaxis.set_major_locator(MultipleLocator(0.5))
plt.savefig('1.tif', dpi=600)

plt.show()
