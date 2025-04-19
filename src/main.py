#-----------------------------
#   RETE BAYESIANA IPOTIZZATA
#-----------------------------
# buying     maint     safety
#    \         |         /
#     \        |        /
#      \       |       /
#       \      |      /
#        \     |     /
#         \    |    /
#          \   |   /
#           \  |  /
#            \ | /
#            class



import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

import signal
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication
from gui.Etivity2Window import Etivity2Window

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
