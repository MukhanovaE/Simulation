from scipy import *
import numpy as np
from Lib.Parametrs import *

def Chi(Current, tipe = '01'):
    Fi = np.pi * Current * M / Fi0  # поток внешнего поля
    E_J = abs(E_J_max * np.cos(Fi) * sqrt(1 + d ** 2 * tan(Fi) ** 2))

    Cog = (E_J / 8 / E_C) ** (1 / 4)
    g01 = 2 * beta * e * Vrms * Cog * np.sqrt(1 / 2) / hbar
    g12 = 2 * beta * e * Vrms * Cog / hbar

    OmP = sqrt(8 * E_C * E_J)  # плазменная частота
    OmQ = OmP - E_C  # omega_{ge}

    chi01 = g01 ** 2 / (OmQ - Om_r)
    chi12 = g12 ** 2 / (OmQ - E_C - Om_r)
    chi = chi01 - chi12 / 2
    chi_approx = g01 ** 2 * alpha / ((OmQ - Om_r) * (OmQ - E_C - Om_r))

    if tipe == '01':
        chi = chi01
    elif tipe == '12':
        chi = chi12
    elif tipe == 'total':
        chi = chi
    elif tipe == 'approx':
        chi = chi_approx
    elif tipe == 'no':
        chi = 0
    return chi


def function_S21(f, Current):
    A = amp * exp(1j * alpha) * exp(-2 * pi * 1j * f * tau)
    Qdel = (Ql / abs(Qc)) * exp(1j * phi)
    fdel = f / (fr0-Chi(Current)) - 1
    Z = 1 + 2 * 1j * Ql * fdel
    ideal = 1 - Qdel / Z
    fS21 = A * ideal
    return fS21