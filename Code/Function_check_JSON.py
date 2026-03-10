def function_check_answer(ChosenAnswer, CurrentOption):        
    """
    Docstring for function_check_answer
    
    :param ChosenAnswer: Die gewählte Antwort vom User (y oder n)
    :param CurrentOption: Ein Dict mit der jetzigen Option & korrekten Antwort
    """

    #Vergleicht Antwort des Spielers mit korrekter Antwort im Dict
    return CurrentOption["correct"] == ChosenAnswer