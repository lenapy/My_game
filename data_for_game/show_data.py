from data_for_game.create_data import read_data_file


def hide_tru_answer(answer):
    return answer.replace(", True", '')


def show_question_and_answers(number_of_question):
    data = read_data_file()
    for ques_and_answ in data:
        if data.index(ques_and_answ) == number_of_question:
            print(ques_and_answ.get('question'))
            for k, val in ques_and_answ.items():
                if isinstance(val, dict):
                    for variant, answer in val.items():
                        print(variant, hide_tru_answer(answer))


def show_tips():
    print("_"*20)
    print("Вы можете использовать подсказки:"
          '\n 1. 50:50'
          '\n 2. Звонок другу'
          '\n 3. Помощь зала')


def calculate_points(is_answer_correct, number_of_question):
    points = [1000, 2000, 3000, 5000,
              10000, 25000, 50000, 100000,
              200000, 400000, 800000, 1000000]
    win_point = points[number_of_question]
    if is_answer_correct == 1:
        players_points = win_point
    elif is_answer_correct == 0 and number_of_question == 4:
        players_points = points[3]
    elif is_answer_correct == 0 and number_of_question == 8:
        players_points = points[7]
    else:
        players_points = 0
    return players_points


def check_true_or_false_answer(player_answer, number_of_question):
    data = read_data_file()
    for item in data:
        if data.index(item) == number_of_question:
            answers = item.get('answers')
            answer = answers.get(player_answer)
            if ", True" in answer:
                return 1
            else:
                return 0


def play_game():
    n = 0
    for i in range(12):
        show_question_and_answers(n)
        show_tips()
        print("_" * 20)
        # print("1. Ответить\n 2. Воспользоваться подсказкой'")
        # input_menu = input("Выберите действие:")
        player_answer = input("Введите ответ:")
        is_answer_correct = check_true_or_false_answer(player_answer, n)
        if is_answer_correct == 1:
            print("Вы выиграли:", calculate_points(is_answer_correct, n), "грн")
            print("_" * 20)
            n += 1
            continue
        else:
            print("Неправильй ответ, Вы заработали", calculate_points(is_answer_correct, n), "грн")
            break

play_game()
