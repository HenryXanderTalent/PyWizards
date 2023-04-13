import random
import requests

def get_categories(): #need for front-end.  returns catgory list json
    """
    Retrieve the trivia categories from OpenTDB API.

    Returns:
        A list of dictionaries, each containing the ID and name of a trivia category.
    """
    cat_url = 'https://opentdb.com/api_category.php'
    cat_response = requests.get(cat_url)
    trivia_categories = cat_response.json()["trivia_categories"]
    return trivia_categories


def print_categories(categories): # change for front-end to display each category
    """
    Print the list of trivia categories along with their IDs.

    Args:
        categories: A list of dictionaries, each containing the ID and name of a trivia category.
    """
    print("Please select a category:")
    for category in categories:
        print(f"{category['id']}: {category['name']}")


def get_user_input(): # change for frontend for input to be user selection
    """
    Retrieve user input for the trivia category ID and difficulty level.

    Returns:
        A tuple containing the trivia category ID and difficulty level.
    """

    # Ideally enter the name rather than ID
    user_question_category = int(input("Enter category ID: "))
    user_difficulty_choice = input("Difficulty: Easy, Medium or Hard: ")
    return user_question_category, user_difficulty_choice


def get_questions(category, difficulty): # returns quiz questions for frontend
    """
    Retrieve the trivia questions from OpenTDB API for the given category and difficulty level.

    Args:
        category: The trivia category ID.
        difficulty: The difficulty level of the trivia questions.

    Returns:
        A list of dictionaries, each containing a trivia question, its answer options, and the correct answer.
    """

    url = "https://opentdb.com/api.php"
    params = {
        "amount": 10,
        "category": category,
        "difficulty": difficulty,
    }
    response = requests.get(url, params=params, timeout=8)
    if response.status_code == 200:
        questions = response.json()["results"]
        return questions
    else:
        raise Exception(f"Error: {response.status_code}")


def ask_questions(questions): # change for frontend
    """
    Ask the trivia questions and check the user's answers.

    Args:
        questions: A list of dictionaries, each containing a trivia question, its answer options, and the correct answer.
    """

    for i, question in enumerate(questions):
        print(f"Question {i+1}: {question['question']}")
        print(f"Options:")
        # Combines the correct and incorrect answer then shuffles
        answer_options = question["incorrect_answers"]
        answer_options.append(question["correct_answer"])
        random.shuffle(answer_options)
        # Return the below for frontend to display each possible answer

        print(answer_options)
        # Takes user input at the moment rather than selecting option
        answer = input("Answer:")
        if answer == question['correct_answer']:
            print(f"Correct: The answer is {question['correct_answer']}")
        else:
            print(f"Wrong: The answer is {question['correct_answer']}")


def run_quiz():
    """
    Run the trivia quiz game by calling the appropriate functions.
    """
    
    categories = get_categories()
    print_categories(categories)
    category, difficulty = get_user_input()
    questions = get_questions(category, difficulty)
    ask_questions(questions)


run_quiz()
