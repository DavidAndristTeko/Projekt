from Function_ImportJSON import function_importJSON
from Function_DisplayQuestion import function_DisplayQuestion
from Function_PlayerFeedback import function_player_feedback
from Function_check_JSON import function_check_answer
from Function_CountPoints import function_CountPoints
from Function_ContinuePlaying import function_ContinuePlaying
from Function_CheckNewImport import function_CheckNewImport

QuestionJSON, RemainingQuestions = function_importJSON("smart10.json", 1)

input("Willkommen zu Smart10! Drücke eine beliebige Taste um das Spiel zu beginnen")

Points = 0
ContinuePlaying = True

while True:
    QuestionNumber = 0
#    UsedQuestions = [] <- Überbleibsel aus PAP dass es nicht mehr braucht

    while QuestionJSON:
        Question, CurrentOption = function_DisplayQuestion(QuestionJSON, QuestionNumber)
#        UsedQuestions.append(Question) <- Überbleibsel aus PAP dass es nicht mehr braucht

        ChosenAnswer = function_player_feedback()
        
        Result = function_check_answer(ChosenAnswer, CurrentOption, QuestionJSON)

        if Result == True:
            print("Korrekt!")
        else:
            print("Leider Falsch :(")

        Points = function_CountPoints(Result, Points)

        print(f"Deine Punktezahl beträgt:{Points}")

        ContinuePlaying = function_ContinuePlaying()

        if ContinuePlaying == False:
            break

        QuestionNumber += 1

    if ContinuePlaying == False:
        break

    QuestionJSON, RemainingQuestions = function_CheckNewImport(RemainingQuestions)
    


        
