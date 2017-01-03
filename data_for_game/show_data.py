import random


from data_for_game.create_data import read_data_file


def get_variants_of_question(number_of_question):
    data = read_data_file()
    for ques_and_answ in data:
        if data.index(ques_and_answ) == number_of_question:
            for k, val in ques_and_answ.items():
                if isinstance(val, dict):
                        return val.items()


def show_question_and_answers(number_of_question):
    data = read_data_file()
    for ques_and_answ in data:
        if data.index(ques_and_answ) == number_of_question:
            print(ques_and_answ.get('question'))
            val = get_variants_of_question(number_of_question)
            for variant, answer in val:
                print(variant, answer.replace(", True", ''))


def show_tips():
    print("_"*20)
    print("\x1b[1;33mВы можете использовать подсказки:\x1b[0m"
          '\n \x1b[1;33m1.\x1b[0m \x1b[1;36m50:50\x1b[0m'
          '\n \x1b[1;33m2.\x1b[0m \x1b[1;36mЗвонок другу\x1b[0m'
          '\n \x1b[1;33m3.\x1b[0m \x1b[1;36mПомощь зала\x1b[0m')


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
    variants = get_variants_of_question(number_of_question)
    for variant, answer in variants:
        if variant == player_answer:
            if ", True" in answer:
                return 1
            else:
                return 0


def check_user_input(user_input):
    variants_of_input = ["A", "B", "C", "D"]
    if user_input in variants_of_input:
        return True
    else:
        return False


def fifty_fifty_tip(number_of_question):
    variants = get_variants_of_question(number_of_question)
    v1, a1 = "", ""
    v2, a2 = "", ""
    for variant, answer in list(variants):
        if ", True" in answer:
            v1, a1 = variant, answer.replace(", True", '')
        else:
            v2, a2 = variant, answer
    print(v1, a1)
    print(v2, a2)


def аsk_the_audience():
    count = 0
    variants = ["A", "B", "C", "D"]
    perсents = [x for x in range(1, 100)]
    for variant in variants:
        p = random.choice(perсents)
        if count + p < 100:
            count += p
            print(variant, p, "%")
        else:
            break


def сall_to_friend(number_of_question):
    variants = get_variants_of_question(number_of_question)
    for variant, answer in list(variants)[:1]:
        print(variant, answer.replace(", True", ''))


def choice_tip(number_of_question, used_tips):
    variants_for_choice = ['1', '2', '3']

    valid = False
    while not valid:
        user_choice = input("\x1b[1;33mВыберите номер подсказки:\x1b[0m")
        if user_choice in variants_for_choice:
            valid = True
            if user_choice not in used_tips:
                used_tips.append(user_choice)
                if user_choice == '1':
                    fifty_fifty_tip(number_of_question)
                elif user_choice == '2':
                    сall_to_friend(number_of_question)
                else:
                    аsk_the_audience()
            else:
                print("\x1b[1;31mВы уже использовали эту подсказку\x1b[0m")
        else:
            print("\x1b[1;31mНеверный ввод\x1b[0m")


def play_game():
    number = 0
    used_tips = list()
    for i in range(12):
        show_question_and_answers(number)
        show_tips()
        print("_" * 20)
        menu = input('\x1b[1;35mЧтобы ответить введите \x1b[1;32m1\x1b[0m\n'
                     '\x1b[1;35mЧтобы воспользоваться подсказкой введите \x1b[1;32m2:\x1b[0m')
        if menu == '1':
            valid = False
            while not valid:
                player_answer = input("Введите ответ:")
                if not check_user_input(player_answer):
                    print('\x1b[1;31mВыберите один из пердложенных вариантов\x1b[0m')
                else:
                    valid = True
                    is_answer_correct = check_true_or_false_answer(player_answer, number)
            if is_answer_correct == 1:
                print("\x1b[1;32mВы выиграли:", calculate_points(is_answer_correct, number), "грн\x1b[0m")
                print("_" * 20)
                number += 1
                continue
            else:
                print("\x1b[1;31mНеправильй ответ, Вы заработали",
                      calculate_points(is_answer_correct, number), "грн\x1b[0m")
                break
        else:
            print('\x1b[5;31m*\x1b[0m'*20)
            choice_tip(number, used_tips)
            print('\x1b[5;31m*\x1b[0m' * 20)

if __name__ == '__main__':
    play_game()
