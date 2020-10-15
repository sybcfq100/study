import numpy as np

data = np.loadtxt('/Users/sybcf/Documents/work/123.txt')
f = data[:,0][0:1001]
r_all = data[:,1]
#np.savetxt('r_all.txt',r_all)
#len(r_all)
arr = r_all.reshape(r_all.shape[0],1)
#np.savetxt('arr.txt',arr)
#len(arr)
arrT = arr.reshape(4,1001)
r_T = arrT.T
#np.save('r_T.txt',r_T)
#print(r_T)
#len(r_T)
f_r =np.c_[f,r_T]
np.savetxt('f_r.txt',f_r)
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set(xlim=[2, 6], ylim=[0, 1], title='An Example Axes',
       ylabel='Y-Axis', xlabel='X-Axis')
plt.plot(f,r_T[:,2],c='r')
plt.show()