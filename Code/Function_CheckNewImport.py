def function_CheckNewImport(RemainingQuestions):
    """
    Docstring for function_CheckNewImport
    
    :param RemainingQuestions: Enthält alle übrigen Frageblöcke aus dem JSON, die der Spieler noch nicht beantwortet hat 
    """

    # nächste Frage holen
    QuestionJSON = [RemainingQuestions.pop(0)]

    return QuestionJSON, RemainingQuestions