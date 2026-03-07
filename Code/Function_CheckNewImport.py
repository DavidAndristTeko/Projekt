def function_CheckNewImport(RemainingQuestions):

    # wenn keine Fragen mehr übrig sind
    if not RemainingQuestions:
        return [], RemainingQuestions

    # nächste Frage holen
    QuestionJSON = [RemainingQuestions.pop(0)]

    return QuestionJSON, RemainingQuestions