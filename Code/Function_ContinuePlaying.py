def function_ContinuePlaying():
    while True:
        #Fragt den Spieler, ob er weiterspielen möchte
        antwort = input("Möchtest du weiter spielen? (y/n): ").strip().lower()

        #Prüft ob Antwort des Spielers eine der erlaubten Antworten ist
        if antwort in ("y", "n"):
            return antwort == "y"

        #Falls Eingabe keine erlaubte Antwort ist, wird spieler auf die erlaubten Antworten hingewiesen
        print("Ungültige Eingabe. Bitte nur 'y' oder 'n'.\n")