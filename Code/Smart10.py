#Modul os wird importiert um die Konsole zwischen Antworten zu "wipen"
import os

#Unsere Funktionen werden importiert
from Function_ImportJSON import function_importJSON
from Function_DisplayQuestion import function_DisplayQuestion
from Function_PlayerFeedback import function_player_feedback
from Function_check_JSON import function_check_answer
from Function_CountPoints import function_CountPoints
from Function_ContinuePlaying import function_ContinuePlaying
from Function_CheckNewImport import function_CheckNewImport

#Erster Fragenblock & restliche Fragenblöcke werden in 2 Variabeln gespeichert
QuestionJSON, RemainingQuestions = function_importJSON("smart10.json", 1)

#User wird aufgefordert das Spiel zu starten
input("Willkommen zu Smart10! Drücke Enter um das Spiel zu beginnen")

#Variabel für Punktezahl wird gesetzt
Points = 0
#Variabel für die erste Schleife wird gesetzt
ContinuePlaying = True

#Schleife läuft so lang wie der Spieler weiterspielen möchte
while ContinuePlaying:
    #Variable welche trackt bei welcher Frage vom Fragenblock wir sind
    QuestionNumber = 0

    #Schleife läuft bis die letzte Frage im Block erreicht ist
    while QuestionNumber < len(QuestionJSON[0]["answers"]):
        
        os.system("cls")
        print()
        print("-" * 40)
        print(f"Option {QuestionNumber+1}/10")
        
        CurrentOption = function_DisplayQuestion(QuestionJSON, QuestionNumber)

        ChosenAnswer = function_player_feedback()

        Result = function_check_answer(ChosenAnswer, CurrentOption)

        if Result:
            print("Korrekt!")
        else:
            print("Leider Falsch :(")

        input("Drücke Enter für die nächste Option...")

        Points = function_CountPoints(Result, Points)

        print(f"Deine Punktezahl beträgt:{Points}")

        ContinuePlaying = function_ContinuePlaying()

        if ContinuePlaying == False:
            break

        QuestionNumber += 1

    if not ContinuePlaying:
        break

    QuestionJSON, RemainingQuestions = function_CheckNewImport(RemainingQuestions)