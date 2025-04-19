import pandas as pd
from scipy.stats import chi2_contingency

# ----------------------------------------------------------
# 1. Caricamento del dataset Car Evaluation da UCI
# ----------------------------------------------------------

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data'
column_names = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class']

# Lettura del file CSV senza intestazioni e con nomi colonna assegnati manualmente
df = pd.read_csv(url, names=column_names)

# ----------------------------------------------------------
# 2. Creazione della tabella di contingenza tra:
#    - buying (prezzo d'acquisto)
#    - class (valutazione del veicolo)
# ----------------------------------------------------------

contingency_table = pd.crosstab(df['buying'], df['class'])

print("\nTabella di contingenza (buying vs class):\n")
print(contingency_table)

# ----------------------------------------------------------
# 3. Applicazione del test del chi-quadro
# ----------------------------------------------------------

chi2, p_value, dof, expected = chi2_contingency(contingency_table)

print("\nRisultati del test del chi-quadro:")
print(f"Valore del chi-quadro: {chi2:.4f}")
print(f"p-value: {p_value:.4f}")
print(f"Gradi di libertà: {dof}")

print("\nFrequenze attese (se buying e class fossero indipendenti):\n")
expected_df = pd.DataFrame(expected, index=contingency_table.index, columns=contingency_table.columns)
print(expected_df)

# ----------------------------------------------------------
# 4. Interpretazione
# ----------------------------------------------------------

alpha = 0.05
if p_value < alpha:
    print(f"\nPoiché p-value = {p_value:.10f} < {alpha}, rifiutiamo l'ipotesi nulla:")
    print("Esiste una dipendenza statisticamente significativa tra 'buying' e 'class'.")
else:
    print(f"\nPoiché p-value = {p_value:.10f} >= {alpha}, non possiamo rifiutare l'ipotesi nulla:")
    print("Non vi è evidenza sufficiente per affermare che 'buying' e 'class' siano dipendenti.")
