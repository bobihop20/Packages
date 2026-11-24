import numpy as np
def expdecay (t, N_0, k):
    N_t=N_0*np.exp(-k*t)
    return N_t

def pdf_normal(x,sigma,mu):
    pdf= 1/(sigma*np.sqrt(2*np.pi))*np.exp(-((x-mu)**2/(2*sigma**2)))
    return pdf

def lintolog(func):
    return np.log(func)