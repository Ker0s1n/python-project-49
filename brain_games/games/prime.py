#!/usr/bin/env python3
from random import randint


TASK_TEXT = 'Answer "yes" if given number is prime. Otherwise answer "no".'
begin_range_question = 0
end_range_question = 101


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    else:
        return True


def generate_question_and_answer():
    questing_number = randint(begin_range_question, end_range_question)
    correct_answer = 'yes' if is_prime(questing_number) else 'no'
    return questing_number, str(correct_answer)
