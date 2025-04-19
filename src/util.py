# Funzione che chiede all'utente rispondere Y o N
def chiedi_azione(msg: str) -> None:
    risposta = input(f"{msg}: [Y/N] ").strip().lower()
    
    if risposta == 'y':
        return True
    elif risposta == 'n':
        return False
    else:
        print("Input non valido. Devi rispondere con 'Y' o 'N'")
        chiedi_azione(msg)  # Riprova se l'input non è valido