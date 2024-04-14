#!/usr/bin/env python3
from random import randint
import prompt


TASK_TEXT = 'What number is missing in the progression?'


def get_user_name():
    print('Welcome to the Brain Games!')
    USER_NAME = prompt.string('May I have your name? ')
    print(f'Hello, {USER_NAME}!')
    print(TASK_TEXT)
    return USER_NAME


def generate_question_and_correct_answer():
    gen_start_progression, gen_step_progression = randint(0, 20), randint(1, 10)
    length_progression = randint(5, 10)
    PROGRESSION = [gen_start_progression]
    for i in range(length_progression):
        PROGRESSION.append(gen_start_progression + gen_step_progression)
        gen_start_progression += gen_step_progression
    gen_correct_answer_index = randint(0, len(PROGRESSION) - 1)
    CORRECT_ANSWER = PROGRESSION[gen_correct_answer_index]
    PROGRESSION[gen_correct_answer_index] = '..'
    QUESTION = ' '.join(str(ELEM) for ELEM in PROGRESSION)
    return QUESTION, str(CORRECT_ANSWER)


def get_user_answer(QUESTION):
    print(f'Question: {QUESTION}')
    GET_ANSWER = prompt.string('Your answer: ')
    return GET_ANSWER


def main():
    user_name = get_user_name()
    COUNT = 0
    while COUNT < 3:
        question, cor_ans = generate_question_and_correct_answer()
        ans = get_user_answer(question)
        if ans == cor_ans:
            print('Correct!')
            COUNT += 1
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{cor_ans}'")
            return print(f'Let\'s try again, {user_name}!')
    print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()
