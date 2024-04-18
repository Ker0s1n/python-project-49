#!/usr/bin/env python3
from random import randint


TASK_TEXT = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return True if number % 2 == 0 else False


def generate_question_and_correct_answer():
    generate_number_for_question = randint(0, 100)
    correct_answer = 'yes' if is_even(generate_number_for_question) else 'no'
    return generate_number_for_question, correct_answer