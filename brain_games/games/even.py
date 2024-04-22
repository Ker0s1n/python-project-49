from random import randint


TASK_TEXT = 'Answer "yes" if the number is even, otherwise answer "no".'
BEGIN_RANGE = 0
END_RANGE = 100


def is_even(number):
    return True if number % 2 == 0 else False


def generate_question_and_answer():
    number_for_question = randint(BEGIN_RANGE, END_RANGE)
    correct_answer = 'yes' if is_even(number_for_question) else 'no'
    return number_for_question, correct_answer
