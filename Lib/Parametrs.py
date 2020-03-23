from scipy.constants import e, h, hbar
from math import pi

C_q = 90e-15
Phi = 0

def E_C():
    return (e)**2/2/C_q/hbar/1e9
def E_J():
    return (2*pi*6+E_C())**2/8/E_C()*cos(pi*Φ)

#parametrs for hamiltonian
OmegaQ = 1.
OmegaR = 1.
OmegaD = 0.
Amp = 0.


g  = 0.05 * 2 * pi  # coupling strength
kappa = 0.005       # cavity dissipation rate
gamma = 0.05        # atom dissipation rate