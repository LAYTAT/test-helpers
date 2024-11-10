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
def generate_question(concept, concept_data):
    definition = concept_data['description']
    choices = [definition]

    # Prepare multiple choices
    while len(choices) < 4:
        random_definition = random.choice([item['description'] for item in concepts.values()])
        if random_definition not in choices:
            choices.append(random_definition)
    random.shuffle(choices)

    # Display the question and choices
    print(f"What is {concept}?")
    for i, choice in enumerate(choices):
        print(f"{i + 1}. {choice}")

    # Take user answer
    try:
        user_answer = int(input("Enter the number of your answer: "))
        if choices[user_answer - 1] == definition:
            print("Correct!\n")
        else:
            print(f"Incorrect. The correct answer was: {definition}\n")
            # Track the incorrect answer
            incorrect_answers[concept] = definition
    except (ValueError, IndexError):
        print("Please enter a valid option.\n")
        incorrect_answers[concept] = definition

    # Mark the question as tested
    concepts[concept]['status'] = "tested"

# Main function to run the quiz
def start_quiz():
    print("AWS Certified AI Practitioner Test Quiz")
    mode = input("Type 'full' for the full test, 'incorrect' for missed questions only, or 'untested' for questions never tested: ").strip().lower()
    
    # Determine question pool based on mode
    if mode == 'incorrect' and incorrect_answers:
        quiz_concepts = {k: {"description": v} for k, v in incorrect_answers.items()}
        print("\nTesting on previously missed questions.\n")
        test_all = input("Would you like to test all incorrect questions? (yes/no): ").strip().lower()
        if test_all == 'yes':
            num_questions = len(quiz_concepts)
        else:
            num_questions = int(input("How many questions would you like to answer? "))
    elif mode == 'untested':
        quiz_concepts = {k: v for k, v in concepts.items() if v['status'] == "never tested"}
        untested_count = len(quiz_concepts)
        if untested_count == 0:
            print("\nCongratulations! All questions have already been tested.\n")
            return
        print(f"\nTesting on questions that have never been tested. {untested_count} questions remain untested.\n")
        num_questions = int(input("How many questions would you like to answer? "))
    elif mode == 'full':
        quiz_concepts = concepts
        print("\nTesting on the full set of questions.\n")
        num_questions = int(input("How many questions would you like to answer? "))
    else:
        print("Invalid input or no missed questions available. Defaulting to the full test.\n")
        quiz_concepts = concepts
        num_questions = int(input("How many questions would you like to answer? "))

    # Shuffle and limit the questions
    quiz_list = list(quiz_concepts.items())
    random.shuffle(quiz_list)
    selected_questions = quiz_list[:num_questions]

    # Ask each question
    for concept, concept_data in selected_questions:
        generate_question(concept, concept_data)

    # Save incorrect answers to a JSON file
    with open('incorrect_answers.json', 'w') as f:
        json.dump(incorrect_answers, f, indent=4)

    # Update the main concepts file with tested status
    with open('all_concepts.json', 'w') as f:
        json.dump(concepts, f, indent=4)
    
    print("\nQuiz completed. Incorrect answers have been saved to 'incorrect_answers.json'.")
    print("All concepts have been updated with their testing status in 'all_concepts.json'.")

# Run the quiz
start_quiz()
