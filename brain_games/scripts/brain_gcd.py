#!/usr/bin/env python3
from random import randint
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Find the greatest common divisor of given numbers.')
    count = 0
    while count < 3:
        oper_1 = randint(-100, 100)
        oper_2 = randint(-100, 100)
        print(f'Question: {oper_1} {oper_2}')
        answ = prompt.string('Your answer: ')
        while oper_1 != oper_2:
            if oper_1 == 0:
                oper_1 = oper_2
            elif oper_2 == 0:
                oper_2 = oper_1
            elif abs(oper_1) > abs(oper_2):
                while abs(oper_1) - abs(oper_2) > 0:
                    oper_1 = abs(oper_1) - abs(oper_2)
            elif abs(oper_2) > abs(oper_1):
                while abs(oper_2) - abs(oper_1) > 0:
                    oper_2 = abs(oper_2) - abs(oper_1)
            elif abs(oper_1) == abs(oper_2):
                oper_1 = abs(oper_1)
            else:
                print('Что-то пошло не так!')
        cor_answ = oper_1
        if int(answ) == cor_answ:
            print('Correct!')
            count += 1
        else:
            print(f"'{answ}' is wrong answer ;(. Correct answer was: '{cor_answ}'.")
            print(f"Let`s try again, {name}!")
            count = 0
    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
