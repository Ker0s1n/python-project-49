#!/usr/bin/env python3
from random import randint
import prompt


task_text = 'Find the greatest common divisor of given numbers.'


def get_user_name():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(task_text)
    return user_name


def generate_question_and_correct_answer():
    gen_operand_1, gen_operand_2 = randint(-100, 100), randint(-100, 100)
    quest = str(f'{gen_operand_1} {gen_operand_2}')
    if gen_operand_1 == 0:
        gen_operand_1 = abs(gen_operand_2)
    if gen_operand_2 == 0 or abs(gen_operand_1) == abs(gen_operand_2):
        gen_operand_1 = abs(gen_operand_1)
    while gen_operand_1 != gen_operand_2:
        largest_of_operands = max(abs(gen_operand_1), abs(gen_operand_2))
        smallest_of_operands = min(abs(gen_operand_1), abs(gen_operand_2))
        gen_operand_1 = largest_of_operands - smallest_of_operands
        gen_operand_2 = smallest_of_operands
    correct_answer = str(gen_operand_1)
    return quest, correct_answer


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
