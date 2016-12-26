import pickle

DATA_FILE = "questions_answers"


def read_data_file():
    try:
        with open(DATA_FILE, 'rb') as f:
            return pickle.load(f)
    except IOError:
        return []


def create_and_save_data(question, dict_of_answers):
    question_and_variants_of_answer = {
        'question': question,
        'answers': dict_of_answers
    }
    data = read_data_file()
    data.append(question_and_variants_of_answer)
    with open(DATA_FILE, 'wb') as f:
        pickle.dump(data, f)


def app_to_create_data_for_game():
    dict_of_answers = {}
    question = input("question:")
    for item in range(4):
        variant = input("variant:")
        answer = input("answer:")
        dict_of_answers[variant] = answer
    create_and_save_data(question, dict_of_answers)
