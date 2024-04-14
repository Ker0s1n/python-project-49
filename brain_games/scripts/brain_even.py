#!/usr/bin/env python3
from random import randint
import prompt


TASK_TEXT = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_user_name():
    print('Welcome to the Brain Games!')
    USER_NAME = prompt.string('May I have your name? ')
    print(f'Hello, {USER_NAME}!')
    print(TASK_TEXT)
    return USER_NAME


def is_even(NUM):
    if NUM % 2 == 0:
        return 'yes'
    else:
        return 'no'


def generate_question_and_correct_answer():
    generate_number_for_question = randint(0, 100)
    CORRECT_ANSWER = is_even(generate_number_for_question)
    return generate_number_for_question, CORRECT_ANSWER


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
