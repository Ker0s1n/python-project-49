#!/usr/bin/env python3
from random import randint
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    while count < 3:
        number = randint(0, 101)
        if number < 2:
            cor_answ = 'no'
        for i in range(2, (number // 2) + 1):
            if number % i == 0:
                cor_answ = 'no'
                break
            else:
                cor_answ = 'yes'
        print(f'Question: {number}')
        answ = prompt.string('Your answer: ')
        if answ == cor_answ:
            print('Correct!')
            count += 1
        else:
            print(f"'{answ}' is wrong answer ;(. Correct answer was: '{cor_answ}'.")
            print(f"Let`s try again, {name}!")
            count = 0
    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
