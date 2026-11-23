import numpy as np
def expdecay (t, N_0, k):
    N_t=N_0*np.exp(-k*t)
    return N_t