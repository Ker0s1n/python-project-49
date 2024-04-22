from random import randint
from math import gcd


TASK_TEXT = 'Find the greatest common divisor of given numbers.'
BEGIN_RANGE = -100
END_RANGE = 100


def generate_question_and_answer():
    operand1 = randint(BEGIN_RANGE, END_RANGE)
    operand2 = randint(BEGIN_RANGE, END_RANGE)
    question = str(f'{operand1} {operand2}')
    correct_answer = str(gcd(operand1, operand2))
    return question, correct_answer
