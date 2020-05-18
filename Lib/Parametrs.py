from scipy import *
import numpy as np

#константы
e = 1.6e-19
Fi0 = 2e-15
hbar = 6.62e-34
c = 300e6

M = 2*pi*0.3e-11

#параетры установки
Ck = 5e-15
Cg = 2e-15
Cq = 90e-15
Cr = 100e-15
Lr = 2e-9
Cs = 10e-15 #чиселко из ниоткуда, но большое


Csum = Cg + Cs
beta = Cg/Csum

E_C = 200e6
alpha = -E_C #anharmonicity


#параметры из эксперимента
fr0 = 6.0e9  #resonator frequency from experiment
Om_r = fr0*2*np.pi
OmQ_exp = 5.3e9 #qubit frequency from experiment


Ql = 3e3
Qc = 2.9e3

tau = 10.**(-9)
phi = pi/6
amp = 1.

#Asymmetric transmon E_J1 = a E_J2
E_J_max = (OmQ_exp+E_C)**2/(8*E_C) #from frequency at sweet spot
a = 10  #inequality of Josephson junctions
E_J1 = E_J_max/(1+a)
E_J2 = a*E_J1
E_Jp = E_J1+E_J2
E_Jm = E_J1-E_J2
d = E_Jm/E_Jp  #SQUID asymmetry


#постоянные коэффициенты
Vrms = np.sqrt(hbar*Om_r/2/Cr)
g = 50e6


g  = 0.05 * 2 * pi  # coupling strength
kappa = 0.005       # cavity dissipation rate
gamma = 0.05        # atom dissipation rate

Omega_Rabi = 2*pi*1e-1