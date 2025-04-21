import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import sys
from contextlib import redirect_stdout
from core.Tee import Tee
from core.chi2 import calculate_chi2_test

def etivity2_compute(var1: str, var2: str, plotFlag=False) -> str:

    buffer = io.StringIO()
    tee = Tee(sys.stdout, buffer)

    with redirect_stdout(tee):  # stampa sia a terminale che in buffer
    
        # ----------------------------------------------------------
        # 1. Caricamento del dataset Car Evaluation da UCI
        # ----------------------------------------------------------

        url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data'
        column_names = [
            'buying',   # Prezzo d'acquisto dell’auto (valori: vhigh, high, med, low)
            'maint',    # Costo di manutenzione annuale (valori: vhigh, high, med, low)
            'doors',    # Numero di porte dell’auto (valori: 2, 3, 4, 5more)
            'persons',  # Capacità massima di passeggeri (valori: 2, 4, more)
            'lug_boot', # Dimensione del bagagliaio (valori: small, med, big)
            'safety',   # Livello di sicurezza stimato (valori: low, med, high)
            'class'     # Valutazione complessiva del veicolo (unacc=unacceptable, acc=acceptable, good=good, vgood=very good)
        ]
        df = pd.read_csv(url, names=column_names)

        # ----------------------------------------------------------
        # 2. Creazione della tabella di contingenza
        # ----------------------------------------------------------

        contingency_table = pd.crosstab(df[var1], df[var2])

        print(f"\nTabella di contingenza ({var1} vs {var2}):\n")
        print(contingency_table)

        # ----------------------------------------------------------
        # 3. Applicazione del test del chi-quadro
        # ----------------------------------------------------------

        chi2, p_value, dof, expected = calculate_chi2_test(contingency_table)
        
        print("\nRisultati del test del chi-quadro:")
        print(f"Valore del chi-quadro: {chi2:.4f}")
        print(f"p-value: {p_value:.4f}")
        print(f"p-value (notazione scientifica): {repr(p_value)}")
        print(f"Gradi di libertà: {dof}")

        print(f"\nFrequenze attese (se {var1} e {var2} fossero indipendenti):\n")
        expected_df = pd.DataFrame(expected, index=contingency_table.index, columns=contingency_table.columns)
        print(expected_df)

        # ----------------------------------------------------------
        # 4. Interpretazione
        # ----------------------------------------------------------

        alpha = 0.05
        if p_value < alpha:
            print(f"\nPoiché p-value = {p_value:.4f} < {alpha}, rifiutiamo l'ipotesi nulla:")
            print(f"Esiste una dipendenza statisticamente significativa tra {var1} e {var2}.")
        else:
            print(f"\nPoiché p-value = {p_value:.4f} >= {alpha}, non possiamo rifiutare l'ipotesi nulla:")
            print(f"Non vi è evidenza sufficiente per affermare che {var1} e {var2} siano dipendenti.")

        # ----------------------------------------------------------
        # 5. Visualizzazione grafica delle tabelle
        # ----------------------------------------------------------

        if (plotFlag):
            fig, axes = plt.subplots(1, 2, figsize=(16, 6))

            # Heatmap delle frequenze osservate
            sns.heatmap(contingency_table, annot=True, fmt="d", ax=axes[0])
            axes[0].set_title(f"Frequenze Osservate ({var1} vs {var2})")
            axes[0].set_xlabel(var1)
            axes[0].set_ylabel(var2)

            # Heatmap delle frequenze attese
            sns.heatmap(expected_df, annot=True, fmt=".1f", ax=axes[1])
            axes[1].set_title(f"Frequenze Attese (se {var1} e {var2} fossero indipendenti)")
            axes[1].set_xlabel(var1)
            axes[1].set_ylabel(var2)

            plt.tight_layout()
            plt.show()
        
        return buffer.getvalue()