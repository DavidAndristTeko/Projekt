import json
from pathlib import Path
from typing import List

# Funktion wird definiert
def function_importJSON(path: str, listenposition: int):
    """
    Lädt eine JSON-Datei mit Struktur:
    {
      "questions": [
        { "question": "...", "answers": [...] },
        ...
      ]
    }
    und gibt die ersten n Fragen zurück.
    """
    # Datei wird geöffnet
    raw = Path(path).read_text(encoding="utf-8")
    # JSON wird geparst/geladen/gelesen
    data = json.loads(raw)

    # JSON muss ein Dictionary sein
    if not isinstance(data, dict):
        raise ValueError("JSON muss ein Dictionary sein.")

    # Fragenliste extrahieren
    if "questions" not in data:
        raise ValueError("JSON enthält keinen Key 'questions'.")
    # extrahierung der Frage aus der Liste
    questions = data["questions"]

    # Prüfen, ob es eine Liste ist
    if not isinstance(questions, list):
        raise ValueError("'questions' muss eine Liste sein.")

    # Prüfen, ob n gültig ist
    if listenposition > len(questions):
        raise ValueError(f"n={listenposition} ist grösser als die Anzahl Fragen im File ({len(questions)}).")
    
    # Gibt die ersten n Elemente zurück
    QuestionJSON = questions[:listenposition]
    questions.pop(listenposition-1)
    return QuestionJSON
