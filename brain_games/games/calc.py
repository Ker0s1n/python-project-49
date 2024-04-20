#!/usr/bin/env python3
from random import randint, choice


TASK_TEXT = 'What is the result of the expression?'
begin_range = 0
end_range = 25
list_of_operands = ['+', '-', '*']


def generate_question_and_answer():
    gen_operand1 = randint(begin_range, end_range)
    gen_operand2 = randint(begin_range, end_range)
    gen_actions_for_operand = choice(list_of_operands)
    match gen_actions_for_operand:
        case '+':
            correct_answer = gen_operand1 + gen_operand2
        case '-':
            correct_answer = gen_operand1 - gen_operand2
        case '*':
            correct_answer = gen_operand1 * gen_operand2
    question = str(f'{gen_operand1} {gen_actions_for_operand} {gen_operand2}')
    return question, str(correct_answer)
