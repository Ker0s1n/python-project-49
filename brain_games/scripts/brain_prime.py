#!/usr/bin/env python3
from random import randint
import prompt


TASK_TEXT = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(NUMBER):
    if NUMBER < 2:
        return 'no'
    for i in range(2, NUMBER // 2 + 1):
        if NUMBER % i == 0:
            return 'no'
    else:
        return 'yes'


def get_user_name():
    print('Welcome to the Brain Games!')
    USER_NAME = prompt.string('May I have your name? ')
    print(f'Hello, {USER_NAME}!')
    print(TASK_TEXT)
    return USER_NAME


def generate_question_and_correct_answer():
    questing_number = randint(0, 101)
    CORRECT_ANSWER = is_prime(questing_number)
    return questing_number, str(CORRECT_ANSWER)


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
