import json
from pathlib import Path
from typing import List


def function_CheckNewImport(RemainingQuestions):
    # Nur importieren, wenn keine Fragen mehr übrig sind
    if RemainingQuestions:
        return False
    

    # Block 1 entfernen und neuer Block wird zu Block 0
    if not RemainingQuestions:
        QuestionJSON = RemainingQuestions[:0]
        RemainingQuestions.pop(0)
        return QuestionJSON, RemainingQuestions