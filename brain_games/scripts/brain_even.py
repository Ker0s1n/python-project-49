#!/usr/bin/env python3
from brain_games.scripts.brain_games import main as brain_games
from random import randrange
import prompt

brain_games()


def main():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        questing_number = randrange(100)
        print(f'Question: {questing_number}')
        answer = prompt.string('Your answer: ')
        correct_answer = 'yes' if questing_number % 2 == 0 else 'no'
        rule_1 = questing_number % 2 == 0 and answer == 'no'
        rule_2 = questing_number % 2 != 0 and answer == 'yes'
        rule_3 = answer not in ('no', 'yes')
        if rule_1 or rule_2 or rule_3:
            print(f'\'{answer}\' is wrong answer ;(. Correct answer \'{correct_answer}\'')
            count = 0
        else:
            print('Correct!')
            count += 1
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
