import sys
import signal
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import ( QApplication, QMainWindow, 
                              QWidget, QVBoxLayout, 
                              QHBoxLayout, QLabel, 
                              QComboBox, QPushButton
                            )

from ml_etivity2 import etivity2_compute  

# Lista di coppie possibili
pairs = [
    ('buying', 'maint'),
    ('buying', 'doors'),
    ('buying', 'persons'),
    ('buying', 'lug_boot'),
    ('buying', 'safety'),
    ('buying', 'class'),
    ('maint', 'doors'),
    ('maint', 'persons'),
    ('maint', 'lug_boot'),
    ('maint', 'safety'),
    ('maint', 'class'),
    ('doors', 'persons'),
    ('doors', 'lug_boot'),
    ('doors', 'safety'),
    ('doors', 'class'),
    ('persons', 'lug_boot'),
    ('persons', 'safety'),
    ('persons', 'class'),
    ('lug_boot', 'safety'),
    ('lug_boot', 'class'),
    ('safety', 'class'),
]

class Etivity2Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Etivity2 - Chi-Quadrato con Reti Bayesiane")
        self.resize(400, 150)

        # Widget centrale
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)

        # Label e ComboBox per la selezione della coppia
        select_layout = QHBoxLayout()
        label = QLabel("Seleziona le variabili:")
        self.combo = QComboBox()

        # Popola il ComboBox con le coppie
        for var1, var2 in pairs:
            self.combo.addItem(f"{var1} vs {var2}", (var1, var2))

        select_layout.addWidget(label)
        select_layout.addWidget(self.combo)
        layout.addLayout(select_layout)

        # Bottone per eseguire il calcolo
        self.run_button = QPushButton("Esegui Chi-Quadrato")
        self.run_button.clicked.connect(self.on_run_clicked)
        layout.addWidget(self.run_button)

        # Label di output
        self.output = QLabel("")
        layout.addWidget(self.output)

    def on_run_clicked(self):
        # Recupera la coppia selezionata
        var1, var2 = self.combo.currentData()

        # Chiama la funzione di calcolo; redireziona l'output nella label
        try:
            result = etivity2_compute(var1, var2, plotFlag=False)
            self.output.setText("Calcolo completato. Controlla la console per i dettagli e i grafici.")
        except Exception as e:
            self.output.setText(f"Errore: {e}")

def handle_sigint(signum, frame):
    """Gestisce il segnale SIGINT per terminare l'applicazione"""
    print("Intercettato Ctrl+C, chiusura dell'applicazione...")
    QApplication.quit()

if __name__ == '__main__':
    print(
    "\n    __  __   _               _____   _     _           _   _             ____  "
    "\n   |  \/  | | |             | ____| | |_  (_) __   __ (_) | |_   _   _  |___ \ "
    "\n   | |\/| | | |      _____  |  _|   | __| | | \ \ / / | | | __| | | | |   __) |"
    "\n   | |  | | | |___  |_____| | |___  | |_  | |  \ V /  | | | |_  | |_| |  / __/ "
    "\n   |_|  |_| |_____|         |_____|  \__| |_|   \_/   |_|  \__|  \__, | |_____|"
    "\n                                                                 |___/         "
    )

    # configura il gestore per il segnale SIGINT
    signal.signal(signal.SIGINT, handle_sigint)

    # Avvia applicazione Qt
    app = QApplication(sys.argv)

    # Per rilevare SIGINT
    timer = QTimer()
    timer.start(100)
    timer.timeout.connect(lambda: None) # tiene vivo il loop di eventi per rilevare SIGINT

    # Lancia finestra grafica
    window = Etivity2Window()
    window.show()
    sys.exit(app.exec_())
