def function_ContinuePlaying():
    while True:
        antwort = input("Möchtest du weiter spielen? (y/n): ").strip().lower()

        if antwort in ("y", "n"):
            return antwort == "y"

        print("Ungültige Eingabe. Bitte nur 'y' oder 'n'.")