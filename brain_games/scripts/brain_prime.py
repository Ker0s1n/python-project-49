#!/usr/bin/env python3
from brain_games.games.prime import TASK_TEXT, generate_question_and_answer
import prompt


def get_user_name():
    print('Welcome to the Brain Games!')
    USER_NAME = prompt.string('May I have your name? ')
    print(f'Hello, {USER_NAME}!')
    print(TASK_TEXT)
    return USER_NAME


def get_user_answer(QUESTION):
    print(f'Question: {QUESTION}')
    GET_ANSWER = prompt.string('Your answer: ')
    return GET_ANSWER


def main():
    user_name = get_user_name()
    COUNT = 0
    while COUNT < 3:
        question, cor_ans = generate_question_and_answer()
        ans = get_user_answer(question)
        if ans == cor_ans:
            print('Correct!')
            COUNT += 1
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{cor_ans}'")
            print(f'Let\'s try again, {user_name}!')
            return
    print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()
