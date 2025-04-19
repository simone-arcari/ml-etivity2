import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency

# ----------------------------------------------------------
# 1. Caricamento del dataset Car Evaluation da UCI
# ----------------------------------------------------------

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data'
column_names = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class']
df = pd.read_csv(url, names=column_names)

# ----------------------------------------------------------
# 2. Creazione della tabella di contingenza
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

# ----------------------------------------------------------
# 4. Visualizzazione grafica delle tabelle
# ----------------------------------------------------------

expected_df = pd.DataFrame(expected, index=contingency_table.index, columns=contingency_table.columns)

# Heatmap delle frequenze osservate
plt.figure(figsize=(10, 6))
sns.heatmap(contingency_table, annot=True, fmt="d", cmap="Blues")
plt.title("Frequenze Osservate (buying vs class)")
plt.xlabel("Classe")
plt.ylabel("Prezzo d'acquisto")
plt.tight_layout()
plt.show()

# Heatmap delle frequenze attese
plt.figure(figsize=(10, 6))
sns.heatmap(expected_df, annot=True, fmt=".1f", cmap="YlOrRd")
plt.title("Frequenze Attese (se buying e class fossero indipendenti)")
plt.xlabel("Classe")
plt.ylabel("Prezzo d'acquisto")
plt.tight_layout()
plt.show()

# ----------------------------------------------------------
# 5. Interpretazione
# ----------------------------------------------------------

alpha = 0.05
if p_value < alpha:
    print(f"\nPoiché p-value = {p_value:.4f} < {alpha}, rifiutiamo l'ipotesi nulla:")
    print("Esiste una dipendenza statisticamente significativa tra 'buying' e 'class'.")
else:
    print(f"\nPoiché p-value = {p_value:.4f} >= {alpha}, non possiamo rifiutare l'ipotesi nulla:")
    print("Non vi è evidenza sufficiente per affermare che 'buying' e 'class' siano dipendenti.")
