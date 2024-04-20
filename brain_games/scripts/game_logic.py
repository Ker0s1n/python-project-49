
import prompt


def get_user_name(TASK_TEXT):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(TASK_TEXT)
    return user_name


def get_user_answer(question):
    print(f'Question: {question}')
    get_answer = prompt.string('Your answer: ')
    return get_answer


def game_logic(TASK_TEXT, generate_question_and_answer):
    user_name = get_user_name(TASK_TEXT)
    COUNT = 0
    while COUNT < 3:
        question, cor_ans = generate_question_and_answer()
        ans = get_user_answer(question)
        if ans == cor_ans:
            print('Correct!')
            COUNT += 1
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{cor_ans}'")
            print(f'Let\'s try again, {user_name}!')
            return
    print(f'Congratulations, {user_name}!')
