#!/usr/bin/env python3
from random import randrange
import prompt


def welcome_user():
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!\nAnswer "yes" if the number is even, otherwise answer "no".')
    return name


def is_even(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def main():
    name = welcome_user()
    count = 0
    while count < 3:
        questing_number = randrange(100)
        answ = prompt.string(f'Question: {questing_number}\nYour answer: ')
        cor_answ = is_even(questing_number)
        if answ == cor_answ:
            print('Correct!')
            count += 1
        else:
            print(f"'{answ}' is wrong answer ;(. Correct answer '{cor_answ}'")
            count = 0
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
