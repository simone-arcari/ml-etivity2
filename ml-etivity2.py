import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency
from util import chiedi_azione


print(
"\n    __  __   _               _____   _     _           _   _             ____  "
"\n   |  \/  | | |             | ____| | |_  (_) __   __ (_) | |_   _   _  |___ \ "
"\n   | |\/| | | |      _____  |  _|   | __| | | \ \ / / | | | __| | | | |   __) |"
"\n   | |  | | | |___  |_____| | |___  | |_  | |  \ V /  | | | |_  | |_| |  / __/ "
"\n   |_|  |_| |_____|         |_____|  \__| |_|   \_/   |_|  \__|  \__, | |_____|"
"\n                                                                 |___/         "
)

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

print("\nFrequenze attese (se buying e class fossero indipendenti):\n")
expected_df = pd.DataFrame(expected, index=contingency_table.index, columns=contingency_table.columns)
print(expected_df)

# ----------------------------------------------------------
# 4. Interpretazione
# ----------------------------------------------------------

alpha = 0.05
if p_value < alpha:
    print(f"\nPoiché p-value = {p_value:.4f} < {alpha}, rifiutiamo l'ipotesi nulla:")
    print("Esiste una dipendenza statisticamente significativa tra 'buying' e 'class'.")
else:
    print(f"\nPoiché p-value = {p_value:.4f} >= {alpha}, non possiamo rifiutare l'ipotesi nulla:")
    print("Non vi è evidenza sufficiente per affermare che 'buying' e 'class' siano dipendenti.")

# ----------------------------------------------------------
# 5. Visualizzazione grafica delle tabelle
# ----------------------------------------------------------

if (chiedi_azione("Visualizzare tabelle di contingenza")):
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # Heatmap delle frequenze osservate
    sns.heatmap(contingency_table, annot=True, fmt="d", ax=axes[0])
    axes[0].set_title("Frequenze Osservate (buying vs class)")
    axes[0].set_xlabel("Classe")
    axes[0].set_ylabel("Prezzo d'acquisto")

    # Heatmap delle frequenze attese
    sns.heatmap(expected_df, annot=True, fmt=".1f", ax=axes[1])
    axes[1].set_title("Frequenze Attese (se buying e class fossero indipendenti)")
    axes[1].set_xlabel("Classe")
    axes[1].set_ylabel("Prezzo d'acquisto")

    plt.tight_layout()
    plt.show()