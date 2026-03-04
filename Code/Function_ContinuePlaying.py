def function_ContinuePlaying():
    print("Möchtest du weiter Spielen? Antworte mit (y/n): ")
    antwort = input().strip()   # entfernt Leerzeichen

    # Eingabe validieren
    while antwort.lower() not in ("y", "n"):
        print("Ungültige Eingabe. Bitte nur 'y' oder 'n' eingeben:")
        antwort = input().strip()

    Answer = antwort.lower()
    
    
    if Answer == "y":
        ContinuePlaying = True
    else:
        ContinuePlaying = False
    return ContinuePlaying