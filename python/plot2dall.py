from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

path = "D:/Results/"
fnames = "COCBsol"
legends = [fnames]
fig = plt.figure()

V = np.loadtxt(path + fnames + ".txt")
#V = np.matrix.transpose(V)
msize = V.shape
Smax = 500
Nt = msize[0]
Nx = msize[1]
S = np.linspace(0, Smax, Nx)

print(msize, Nx, Nt)

for i in range(0, Nt, 5):
    plt.plot(S, V[i, :])

plt.legend(legends, loc = "upper right")
plt.xlabel("Stock Price")
plt.ylabel("Convertible Bond Value")
#axes = plt.gca()
#axes.set_xlim([20, 160])
#axes.set_ylim([50, 160])
plt.show()