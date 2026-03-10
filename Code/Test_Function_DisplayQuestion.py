import pytest 
from Function_DisplayQuestion import function_DisplayQuestion

QuestionJSON = [{'question': 'Ist dieses Tier ein Säugetier?', 'answers': [{'text': 'Elefant', 'correct': 'y'}, {'text': 'Hai', 'correct': 'n'}, {'text': 'Giraffe', 'correct': 'y'}, {'text': 'Krokodil', 'correct': 'n'}, {'text': 'Delfin', 'correct': 'y'}, {'text': 'Pinguin', 'correct': 'n'}, {'text': 'Fledermaus', 'correct': 'y'}, {'text': 'Schlange', 'correct': 'n'}, {'text': 'Wal', 'correct': 'y'}, {'text': 'Krabbe', 'correct': 'n'}]}]
 
def test_function_DisplayQuestion():
    assert function_DisplayQuestion(QuestionJSON, 0) == {'text': 'Elefant', 'correct': 'y'}
    assert function_DisplayQuestion(QuestionJSON, 2) == {'text': 'Giraffe', 'correct': 'y'}
    assert function_DisplayQuestion(QuestionJSON, 7) == {'text': 'Schlange', 'correct': 'n'}