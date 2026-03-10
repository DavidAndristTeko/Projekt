def function_CountPoints(Result, Points):
    """
    Docstring for function_CountPoints

    :param Result: Angabe ob Antwort des Spielers korrekt war
    :param Points: Anzahl Punkte die der Spieler bereits hat
    """
    #Erhöht Punktezahl um 1 bei korrekter Antwort. Bei inkorrekter Antwort, wird Punktezahl auf 0 gesetzt
    if Result:
        Points += 1
    else:
        Points = 0
    
    return Points