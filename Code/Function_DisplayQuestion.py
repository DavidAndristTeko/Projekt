def function_DisplayQuestion(QuestionJSON, QuestionNumber):
    Question = QuestionJSON["question"]
    Answers = QuestionJSON["answers"]

    print(Question)
    
    CurrentOption = Answers[QuestionNumber]
    print(CurrentOption["text"])

    return Question, CurrentOption

#Test =    {
        "question": "Ist dieses Tier ein Säugetier?",
        "answers": [
            {
            "text": "Elefant",
            "correct": True
            },
            {
            "text": "Hai",
            "correct": False
            },
            {
            "text": "Giraffe",
            "correct": True
            },
            {
            "text": "Krokodil",
            "correct": False
            },
            {
            "text": "Delfin",
            "correct": True
            },
            {
            "text": "Pinguin",
            "correct": False
            },
            {
            "text": "Fledermaus",
            "correct": True
            },
            {
            "text": "Schlange",
            "correct": False
            },
            {
            "text": "Wal",
            "correct": True
            },
            {
            "text": "Krabbe",
            "correct": False
            }
        ]
        }

#function_DisplayQuestion(Test, 0)