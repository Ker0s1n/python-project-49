#!/usr/bin/env python3
from random import randint


TASK_TEXT = 'What number is missing in the progression?'


def generate_question_and_correct_answer():
    gen_start_progression, gen_step_progression = randint(0, 20), randint(1, 10)
    length_progression = randint(5, 10)
    progression = [gen_start_progression]
    for i in range(length_progression):
        progression.append(gen_start_progression + gen_step_progression)
        gen_start_progression += gen_step_progression
    gen_correct_answer_index = randint(0, len(progression) - 1)
    correct_answer = progression[gen_correct_answer_index]
    progression[gen_correct_answer_index] = '..'
    question = ' '.join(str(element) for element in progression)
    return question, str(correct_answer)