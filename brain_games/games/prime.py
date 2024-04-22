from random import randint


TASK_TEXT = 'Answer "yes" if given number is prime. Otherwise answer "no".'
BEGIN_RANGE = 0
END_RANGE = 101


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    else:
        return True


def generate_question_and_answer():
    questing_number = randint(BEGIN_RANGE, END_RANGE)
    correct_answer = 'yes' if is_prime(questing_number) else 'no'
    return questing_number, str(correct_answer)
