import numpy as np
from scipy.stats import chi2 as chi2_dist

def calculate_chi2_test(observed):
    observed = np.asarray(observed)
    
    # Totali riga e colonna
    row_totals = observed.sum(axis=1, keepdims=True)
    col_totals = observed.sum(axis=0, keepdims=True)
    grand_total = observed.sum()
    
    # Valori attesi
    expected = row_totals @ col_totals / grand_total  # prodotto matriciale
    
    # Calcolo del chi quadrato
    chi2 = ((observed - expected) ** 2 / expected).sum()
    
    # Gradi di libertà: (righe - 1) * (colonne - 1)
    dof = (observed.shape[0] - 1) * (observed.shape[1] - 1)
    
    # p-value (distribuzione chi quadrato)
    p_value = chi2_dist.sf(chi2, dof)  # sf = 1 - cdf

    return chi2, p_value, dof, expected
