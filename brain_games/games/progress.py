from random import randint


TASK_TEXT = 'What number is missing in the progression?'
BEGIN_RANGE_START = 0
END_RANGE_START = 20
BEGIN_RANGE_STEP = 1
END_RANGE_STEP = 10
BEGIN_RANGE_LEN = 5
END_RANGE_LEN = 10


def generate_question_and_answer():
    start_progression = randint(BEGIN_RANGE_START, END_RANGE_START)
    step_progression = randint(BEGIN_RANGE_STEP, END_RANGE_STEP)
    length_progression = randint(BEGIN_RANGE_LEN, END_RANGE_LEN)
    progression = [start_progression]
    for i in range(length_progression):
        progression.append(start_progression + step_progression)
        start_progression += step_progression
    correct_answer_index = randint(0, len(progression) - 1)
    correct_answer = progression[correct_answer_index]
    progression[correct_answer_index] = '..'
    question = ' '.join(str(element) for element in progression)
    return question, str(correct_answer)
