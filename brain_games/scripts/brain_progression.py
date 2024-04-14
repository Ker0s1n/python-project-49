#!/usr/bin/env python3
from random import randint
import prompt


task_text = 'What number is missing in the progression?'


def get_user_name():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(task_text)
    return user_name


def generate_question_and_correct_answer():
    gen_start_progression, gen_step_progression = randint(0, 20), randint(1, 10)
    length_progression = randint(5, 10)
    progression = [gen_start_progression]
    for i in range(length_progression):
        progression.append(gen_start_progression + gen_step_progression)
        gen_start_progression += gen_step_progression
    gen_correct_answer_index = randint(0, len(progression) - 1)
    correct_answ = progression[gen_correct_answer_index]
    progression[gen_correct_answer_index] = '..'
    question = ' '.join(str(elem) for elem in progression)
    return question, str(correct_answ)


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
