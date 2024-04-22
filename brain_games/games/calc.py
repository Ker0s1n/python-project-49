from random import randint, choice


TASK_TEXT = 'What is the result of the expression?'
BEGIN_RANGE = 0
END_RANGE = 25
OPERATORS = ['+', '-', '*']


def generate_question_and_answer():
    operand1 = randint(BEGIN_RANGE, END_RANGE)
    operand2 = randint(BEGIN_RANGE, END_RANGE)
    operator = choice(OPERATORS)
    match operator:
        case '+':
            correct_answer = operand1 + operand2
        case '-':
            correct_answer = operand1 - operand2
        case '*':
            correct_answer = operand1 * operand2
    question = str(f'{operand1} {operator} {operand2}')
    return question, str(correct_answer)
