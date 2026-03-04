def check_answer(ChosenAnswer, CurrentOption, QuestionJSON):
    Result = False  # default
    # Convert user input zu boolean
    user_bool = True if ChosenAnswer.lower() == "y" else False
    for question in QuestionJSON.get("questions", []):
        for answer in question.get("answers", []):
            if answer.get("text") == CurrentOption:
                correct_value = answer.get("correct", False)
                # beide boolean values werden verglichen
                Result = (correct_value == user_bool)
                return Result  # stop wenn gefunden
    return Result  # wenn nichts matched