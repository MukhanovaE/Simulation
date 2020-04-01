from scipy import *
from qutip import *
from sympy import *
from matplotlib import *
import matplotlib.pyplot as plt

from matplotlib import colors
from matplotlib import cm

from Lib.Parametrs import *
import Lib.Bloch_sphere as bloch


#hamiltonian of harmonic oscillator

Ec = 1.
El = 1.
n = 0.
phi = np.linspace(-np.pi, np.pi, 100)

Hh = 4*Ec*n**2 + El*phi**2/2
def phit(h):
    phit = np.sqrt(2*h/El)
    return phit


fig = plt.figure()
n = 3
#plt.rcParams['figure.figsize'] = [n, n]
ax = fig.add_subplot(1, 1, 1)
ax.set_ylabel(r'Энергия [$\hbar \omega_{r}$]')
ax.set_xlabel('Фаза, $\phi$')
plt.ylim(-0.2,4.5)

plt.xticks([-np.pi, -np.pi/2, 0, np.pi, np.pi/2], ['$-\pi$', '$-\pi$/2' , '0', '$\pi$/2', '$\pi$'])


ax.hlines(1-0.5, -phit(1-0.5), phit(1-0.5), 'r', linewidth = 0.6)
ax.hlines(2-0.5, -phit(2-0.5), phit(2-0.5), 'r', linewidth = 0.6)
ax.hlines(3-0.5, -phit(3-0.5), phit(3-0.5), 'r', linewidth = 0.6)
ax.hlines(4-0.5, -phit(4-0.5), phit(4-0.5), 'r', linewidth = 0.6)


ax.annotate("", xy=(0, 1+0.5), xytext=(0, 0+0.5), arrowprops=dict(arrowstyle="<|-|>"))
ax.annotate("", xy=(0, 2+0.5), xytext=(0, 1+0.5), arrowprops=dict(arrowstyle="<|-|>"))
ax.annotate("", xy=(0, 3+0.5), xytext=(0, 2+0.5), arrowprops=dict(arrowstyle="<|-|>"))
ax.annotate("", xy=(0, 4+0.5), xytext=(0, 3+0.5), arrowprops=dict(arrowstyle="<|-|>"))

plt.text(-1.2, 1.35+0.5, r'$\hbar \omega_{r}$', fontsize=13)

plt.plot(phi,Hh, 'r')
plt.show()