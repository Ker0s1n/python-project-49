import prompt


def get_user_name(task_text):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(task_text)
    return user_name


def get_user_answer(question):
    print(f'Question: {question}')
    get_answer = prompt.string('Your answer: ')
    return get_answer


def play_game(module):
    user_name = get_user_name(module.TASK_TEXT)
    count_correct_answers = 0
    number_correct_answers_to_win = 3
    while count_correct_answers < number_correct_answers_to_win:
        question, cor_ans = module.generate_question_and_answer()
        ans = get_user_answer(question)
        if ans == cor_ans:
            print('Correct!')
            count_correct_answers += 1
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{cor_ans}'")
            print(f'Let\'s try again, {user_name}!')
            return
    print(f'Congratulations, {user_name}!')
