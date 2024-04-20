#!/usr/bin/env python3
from brain_games.games.progress import TASK_TEXT, generate_question_and_answer
from brain_games.scripts.game_logic import game_logic


def main():
    game_logic(TASK_TEXT, generate_question_and_answer)


if __name__ == '__main__':
    main()
