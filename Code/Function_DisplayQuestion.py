def function_DisplayQuestion(QuestionJSON, QuestionNumber):
    Question = QuestionJSON[0]["question"]
    Answers = QuestionJSON[0]["answers"]

    print(Question)
    
    CurrentOption = Answers[QuestionNumber]
    print(CurrentOption["text"])

    return CurrentOption