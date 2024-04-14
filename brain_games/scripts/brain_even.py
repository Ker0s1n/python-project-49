#!/usr/bin/env python3
from random import randint
import prompt


task_text = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_user_name():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(task_text)
    return user_name


def is_even(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def generate_question_and_correct_answer():
    generate_number_for_question = randint(0, 100)
    correct_answer = is_even(generate_number_for_question)
    return generate_number_for_question, correct_answer


def get_user_answer(question):
    print(f'Question: {question}')
    get_answer = prompt.string('Your answer: ')
    return get_answer


def main():
    user_name = get_user_name()
    count = 0
    while count < 3:
        question, cor_ans = generate_question_and_correct_answer()
        ans = get_user_answer(question)
        if ans == cor_ans:
            print('Correct!')
            count += 1
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{cor_ans}'")
            return print(f'Let\'s try again, {user_name}!')
    print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()
