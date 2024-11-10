import random
import json
import os

# Load concepts from the JSON file
with open('all_concepts.json', 'r') as f:
    concepts = json.load(f)

# Load or initialize the incorrect answers list
if os.path.exists('incorrect_answers.json'):
    with open('incorrect_answers.json', 'r') as f:
        incorrect_answers = json.load(f)
else:
    incorrect_answers = {}

# Function to create a quiz question
def generate_question(concepts_dict):
    correct_concept = random.choice(list(concepts_dict.keys()))
    correct_definition = concepts_dict[correct_concept]

    # Prepare multiple choices
    choices = [correct_definition]
    while len(choices) < 4:
        random_definition = random.choice(list(concepts.values()))
        if random_definition not in choices:
            choices.append(random_definition)
    random.shuffle(choices)

    # Display the question and choices
    print(f"What is {correct_concept}?")
    for i, choice in enumerate(choices):
        print(f"{i + 1}. {choice}")

    # Take user answer
    try:
        user_answer = int(input("Enter the number of your answer: "))
        if choices[user_answer - 1] == correct_definition:
            print("Correct!\n")
        else:
            print(f"Incorrect. The correct answer was: {correct_definition}\n")
            # Track the incorrect answer
            incorrect_answers[correct_concept] = correct_definition
    except (ValueError, IndexError):
        print("Please enter a valid option.\n")
        # Track the incorrect answer due to invalid input
        incorrect_answers[correct_concept] = correct_definition

# Main function to run the quiz
def start_quiz():
    print("AWS Certified AI Practitioner Test Quiz")
    mode = input("Type 'full' for the full test or 'incorrect' to test only on previously missed questions: ").strip().lower()
    
    if mode == 'incorrect' and incorrect_answers:
        quiz_concepts = incorrect_answers
        print("\nTesting on previously missed questions.\n")
    elif mode == 'full':
        quiz_concepts = concepts
        print("\nTesting on the full set of questions.\n")
    else:
        print("Invalid input or no previously missed questions available. Defaulting to the full test.\n")
        quiz_concepts = concepts

    num_questions = int(input("How many questions would you like to answer? "))
    for _ in range(num_questions):
        generate_question(quiz_concepts)

    # Save incorrect answers to a JSON file
    with open('incorrect_answers.json', 'w') as f:
        json.dump(incorrect_answers, f, indent=4)
    print("\nQuiz completed. Incorrect answers have been saved to 'incorrect_answers.json'.")

# Run the quiz
start_quiz()

