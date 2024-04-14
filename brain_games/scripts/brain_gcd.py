#!/usr/bin/env python3
from random import randint
import prompt


TASK_TEXT = 'Find the greatest common divisor of given numbers.'


def get_user_name():
    print('Welcome to the Brain Games!')
    USER_NAME = prompt.string('May I have your name? ')
    print(f'Hello, {USER_NAME}!')
    print(TASK_TEXT)
    return USER_NAME


def generate_question_and_correct_answer():
    gen_operand1, gen_operand2 = randint(-100, 100), randint(-100, 100)
    QUESTION = str(f'{gen_operand1} {gen_operand2}')
    if gen_operand1 == 0:
        gen_operand1 = abs(gen_operand2)
    if gen_operand2 == 0 or abs(gen_operand1) == abs(gen_operand2):
        gen_operand1 = abs(gen_operand1)
    while gen_operand1 != gen_operand2:
        LARGEST_OF_OPERANDS = max(abs(gen_operand1), abs(gen_operand2))
        SMALLEST_OF_OPERANDS = min(abs(gen_operand1), abs(gen_operand2))
        gen_operand1 = LARGEST_OF_OPERANDS - SMALLEST_OF_OPERANDS
        gen_operand2 = SMALLEST_OF_OPERANDS
    CORRECT_ANSWER = str(gen_operand1)
    return QUESTION, CORRECT_ANSWER


def get_user_answer(QUESTION):
    print(f'Question: {QUESTION}')
    GET_ANSWER = prompt.string('Your answer: ')
    return GET_ANSWER


def main():
    user_name = get_user_name()
    COUNT = 0
    while COUNT < 3:
        question, cor_ans = generate_question_and_correct_answer()
        ans = get_user_answer(question)
        if ans == cor_ans:
            print('Correct!')
            COUNT += 1
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{cor_ans}'")
            return print(f'Let\'s try again, {user_name}!')
    print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()
