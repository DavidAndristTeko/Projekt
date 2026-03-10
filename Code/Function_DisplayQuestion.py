def function_DisplayQuestion(QuestionJSON, QuestionNumber):
    """
    Docstring for function_DisplayQuestion

    :param QuestionJSON: Fragenblock der Aktuell beantwortet wird
    :param QuestionNumber: Angabe welche Option vom Fragenblock beantwortet wird
    """
    #Frage & dazugehörige Optionen werden separat gespeichert
    Question = QuestionJSON[0]["question"]
    Options = QuestionJSON[0]["answers"]

    #Frage wird ausgegeben
    print(Question,"\n")
    
    #Option welche beantwortet werden soll, wird ausgegeben
    CurrentOption = Options[QuestionNumber]
    print(CurrentOption["text"],"\n")

    return CurrentOption