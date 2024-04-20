#!/usr/bin/env python3
from random import randint


TASK_TEXT = 'What number is missing in the progression?'
begin_range_start = 0
end_range_start = 20
begin_range_step = 1
end_range_step = 10
begin_range_len = 5
end_range_len = 10


def generate_question_and_answer():
    gen_start_progression = randint(begin_range_start, end_range_start)
    gen_step_progression = randint(begin_range_step, end_range_step)
    length_progression = randint(begin_range_len, end_range_len)
    progression = [gen_start_progression]
    for i in range(length_progression):
        progression.append(gen_start_progression + gen_step_progression)
        gen_start_progression += gen_step_progression
    gen_correct_answer_index = randint(0, len(progression) - 1)
    correct_answer = progression[gen_correct_answer_index]
    progression[gen_correct_answer_index] = '..'
    question = ' '.join(str(element) for element in progression)
    return question, str(correct_answer)
