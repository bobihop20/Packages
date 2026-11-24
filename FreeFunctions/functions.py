import numpy as np
def expdecay (t, N_0, k):
    N_t=N_0*np.exp(-k*t)
    return N_t

def pdf_normal(x,sigma,mu):
    """Calculates the PDF of a normal distribution"""
    pdf= 1/(sigma*np.sqrt(2*np.pi))*np.exp(-((x-mu)**2/(2*sigma**2)))
    return pdf

def lognormal_pdf(x: float, mu: float, sigma: float) -> float:
    """Calculates the PDF of a log-normal distribution."""
    if x <= 0:
        return 0.0
    if sigma <= 0:
        raise ValueError("Standard deviation (sigma) must be greater than 0.")

    coefficient = 1.0 / (x * sigma * np.sqrt(2 * np.pi))
    exponent = -((np.log(x) - mu) ** 2) / (2 * (sigma**2))
    return coefficient * np.exp(exponent)

def lintolog(func):
    return np.log(func)