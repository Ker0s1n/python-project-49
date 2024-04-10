#!/usr/bin/env python3
from random import randint
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    count = 0
    while count < 3:
        step = randint(1,10)
        start = randint(0, 20)
        length = randint(5, 10)
        list = [start]
        for i in range(length):
            list.append(start + step)
            start += step
        correct = randint(0, len(list)-1)
        cor_answ = list[correct]
        list[correct] = '..'
        list = ' '.join(str(elem) for elem in list)
        print(f'Question: {list}')
        answ = prompt.string('Your answer: ')
        if int(answ) == int(cor_answ):
            print('Correct!')
            count += 1
        else:
            print(f"'{answ}' is wrong answer ;(. Correct answer was: '{cor_answ}'.")
            print(f"Let`s try again, {name}!")
            count = 0
    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
