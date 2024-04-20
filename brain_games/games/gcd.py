#!/usr/bin/env python3
from random import randint
from math import gcd


TASK_TEXT = 'Find the greatest common divisor of given numbers.'
begin_range = -100
end_range = 100


def generate_question_and_answer():
    gen_operand1 = randint(begin_range, end_range)
    gen_operand2 = randint(begin_range, end_range)
    question = str(f'{gen_operand1} {gen_operand2}')
    correct_answer = str(gcd(gen_operand1, gen_operand2))
    return question, correct_answer
