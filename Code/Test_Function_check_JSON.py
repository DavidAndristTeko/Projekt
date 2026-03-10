import pytest 
from Function_check_JSON import function_check_answer
 
yes = "y"
no = "no"
Option_1 = {'text': 'Elefant', 'correct': 'y'}
Option_2 = {'text': 'Elefant', 'correct': 'n'}

def test_function_check_answer():
    assert function_check_answer(yes, Option_1) == True
    assert function_check_answer(yes, Option_2) == False
    assert function_check_answer(no, Option_1) == False
    assert function_check_answer(no, Option_2) == True