#!/usr/bin/env python3
from random import randint


TASK_TEXT = 'Answer "yes" if the number is even, otherwise answer "no".'
begin_range = 0
end_range = 100


def is_even(number):
    return True if number % 2 == 0 else False


def generate_question_and_answer():
    generate_number_for_question = randint(begin_range, end_range)
    correct_answer = 'yes' if is_even(generate_number_for_question) else 'no'
    return generate_number_for_question, correct_answer
