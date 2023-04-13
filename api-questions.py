import random
import requests

url = "https://opentdb.com/api.php"

cat_url = 'https://opentdb.com/api_category.php'

cat_response = requests.get(cat_url)
trivia_categories = cat_response.json()["trivia_categories"]

print("Please select a category:")
for category in trivia_categories:
    print(f"{category['id']}: {category['name']}")

user_question_category = int(input("Enter category ID: "))
user_difficulty_choice = input("Pick a difficulty: Easy, Medium or Hard: ")

params = {
    "amount": 10, 
    "category": {user_question_category}, 
    "difficulty": "{user_difficulty_choice}",     
}

response = requests.get(url, params=params)

if response.status_code == 200:
    questions = response.json()["results"]
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
else:
    print(f"Error: {response.status_code}")
