#!/usr/bin/env python3
from random import randint, choice


TASK_TEXT = 'What is the result of the expression?'


def generate_question_and_answer():
    gen_operand1, gen_operand2 = randint(0, 25), randint(0, 25)
    gen_actions_for_operand = choice(['+', '-', '*'])
    match gen_actions_for_operand:
        case '+':
            correct_answer = gen_operand1 + gen_operand2
        case '-':
            correct_answer = gen_operand1 - gen_operand2
        case '*':
            correct_answer = gen_operand1 * gen_operand2
    question = str(f'{gen_operand1} {gen_actions_for_operand} {gen_operand2}')
    return question, str(correct_answer)
