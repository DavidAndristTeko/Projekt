def player_feedback():
    print("Bitte gib deine Antwort ein (y/n): ")
    antwort = input().strip()   # entfernt Leerzeichen

    # Eingabe validieren
    while antwort.lower() not in ("y", "n"):
        print("Ungültige Eingabe. Bitte nur 'y' oder 'n' eingeben:")
        antwort = input().strip()

    ChosenAnswer = antwort.lower()
    return ChosenAnswer