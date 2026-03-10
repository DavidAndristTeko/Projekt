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
        
        #Diverse Aktionen um das User-Interface angenehmer zu gestalten
        os.system("cls")
        print()
        print("-" * 40)
        print(f"Option {QuestionNumber+1}/10\n")

        #Frage & Option die Beantwortet werden soll, werden angezeigt. Dict mit der Option & Antwort wird gespeichert.
        CurrentOption = function_DisplayQuestion(QuestionJSON, QuestionNumber)

        #Spieler wird aufgefordert Option zu beantworten. Antwort wird gespeichert.
        ChosenAnswer = function_player_feedback()

        #Es wird geprüft, ob die Antwort korrekt ist. Das Resultat wird gespeichert.
        Result = function_check_answer(ChosenAnswer, CurrentOption)

        #Dem Spieler wird ausgegeben, ob Antwort korrekt oder falsch war.
        if Result:
            print("\nKorrekt!\n")
        else:
            print("\nLeider Falsch :(\n")

        input("Drücke Enter für die nächste Option...\n")

        #Punkte werden gezählt, gespeichert & ausgegeben
        Points = function_CountPoints(Result, Points)
        print(f"Deine Punktezahl beträgt:{Points}\n")

        #Der Spieler wird gefragt, ob er weiterspielen möchte. Antwort wird gespeichert.
        ContinuePlaying = function_ContinuePlaying()
        
        #Falls der Spieler nicht weiterspielen möchte, wird das Spiel beendet
        if not ContinuePlaying:
            break
        
        #Variable für das tracken des Frageblocks, wird um eins erhöht
        QuestionNumber += 1

    if not ContinuePlaying:
        break
    
    #Falls Fragenblock leer ist, wird ein neuer Fragenblock geladen
    QuestionJSON, RemainingQuestions = function_CheckNewImport(RemainingQuestions)

print("\nDanke fürs Spielen! Du hast eine Punktezahl von",Points,"erziehlt. Glückwunsch! :)\n")