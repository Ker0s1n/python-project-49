#!/usr/bin/env python3
from random import randrange
import prompt


def main():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        questing_number = randrange(100)
        print(f'Question: {questing_number}')
        answ = prompt.string('Your answer: ')
        corr_answ = 'yes' if questing_number % 2 == 0 else 'no'
        rule_1 = questing_number % 2 == 0 and answ == 'no'
        rule_2 = questing_number % 2 != 0 and answ == 'yes'
        rule_3 = answ not in ('no', 'yes')
        if rule_1 or rule_2 or rule_3:
            print(f"'{answ}' is wrong answer ;(. Correct answer '{corr_answ}'")
            count = 0
        else:
            print('Correct!')
            count += 1
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
