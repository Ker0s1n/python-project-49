#!/usr/bin/env python3
from random import randint, choice
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    count = 0
    while count < 3:
        oper_1 = randint(0, 25)
        oper_2 = randint(0, 25)
        operation = choice(['+', '-', '*'])
        match operation:
            case '+':
                cor_answ = oper_1 + oper_2
            case '-':
                cor_answ = oper_1 - oper_2
            case '*':
                cor_answ = oper_1 * oper_2
        print(f'Question: {oper_1} {operation} {oper_2}')
        answ = prompt.string('Your answer: ')
        if int(answ) == cor_answ:
            print('Correct!')
            count += 1
        else:
            print(f"'{answ}'is wrong answer ;(. Correct answer was: '{cor_answ}'.")
            print(f"Let`s try again, {name}!")
            count = 0
    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
