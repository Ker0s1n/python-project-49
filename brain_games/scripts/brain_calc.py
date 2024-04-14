#!/usr/bin/env python3
from random import randint, choice
import prompt


TASK_TEXT = 'What is the result of the expression?'


def get_user_name():
    print('Welcome to the Brain Games!')
    USER_NAME = prompt.string('May I have your name? ')
    print(f'Hello, {USER_NAME}!')
    print(TASK_TEXT)
    return USER_NAME


def generate_question_and_correct_answer():
    gen_operand1, gen_operand2 = randint(0, 25), randint(0, 25)
    gen_actions_for_operand = choice(['+', '-', '*'])
    match gen_actions_for_operand:
        case '+':
            CORRECT_ANSWER = gen_operand1 + gen_operand2
        case '-':
            CORRECT_ANSWER = gen_operand1 - gen_operand2
        case '*':
            CORRECT_ANSWER = gen_operand1 * gen_operand2
    QUESTION = str(f'{gen_operand1} {gen_actions_for_operand} {gen_operand2}')
    return QUESTION, str(CORRECT_ANSWER)


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
