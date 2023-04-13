import random
import requests

def get_categories():
    cat_url = 'https://opentdb.com/api_category.php'
    cat_response = requests.get(cat_url)
    trivia_categories = cat_response.json()["trivia_categories"]
    return trivia_categories

def print_categories(categories):
    print("Please select a category:")
    for category in categories:
        print(f"{category['id']}: {category['name']}")

def get_user_input():
    user_question_category = int(input("Enter category ID: "))
    user_difficulty_choice = input("Difficulty: Easy, Medium or Hard: ")
    return user_question_category, user_difficulty_choice

def get_questions(category, difficulty):
    url = "https://opentdb.com/api.php"
    params = {
        "amount": 10, 
        "category": category, 
        "difficulty": difficulty,     
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        questions = response.json()["results"]
        return questions
    else:
        raise Exception(f"Error: {response.status_code}")


def ask_questions(questions):
    for i, question in enumerate(questions):
        print(f"Question {i+1}: {question['question']}")
        print(f"Options:")
        answer_options = question["incorrect_answers"]
        answer_options.append(question["correct_answer"])
        random.shuffle(answer_options)
        print(answer_options)
        answer = input("Answer:")
        if answer == question['correct_answer']:
            print(f"Correct: The answer is {question['correct_answer']}")
        else:
            print(f"Wrong: The answer is {question['correct_answer']}")

def run_quiz():
    categories = get_categories()
    print_categories(categories)
    category, difficulty = get_user_input()
    questions = get_questions(category, difficulty)
    ask_questions(questions)

run_quiz()
