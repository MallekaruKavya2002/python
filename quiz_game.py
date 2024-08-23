print("Welcome to the Quiz Game!")
print("Rules:")
print("1. Choose the correct answer from the options.")
print("2. For fill-in-the-blank questions, type your answer.")

# Load quiz questions
quiz_questions = {
    "What is the capital of France?": {
        "options": ["Paris", "London", "Berlin", "Rome"],
        "correct": "Paris"
    },
    "Who painted the Mona Lisa?": {
        "options": ["Leonardo da Vinci", "Michelangelo", "Raphael", "Caravaggio"],
        "correct": "Leonardo da Vinci"
    },
    "What is the largest planet in our solar system?": {
        "options": ["Earth", "Saturn", "Jupiter", "Uranus"],
        "correct": "Jupiter"
    },
    "What is the smallest country in the world?": {
        "fill_in": True,
        "correct": "Vatican City"
    }
}

# Initialize score
score = 0

# Present quiz questions
for question, details in quiz_questions.items():
    print("\n" + question)
    if "options" in details:
        for i, option in enumerate(details["options"]):
            print(f"{i+1}. {option}")
        answer = input("Choose your answer (1/2/3/4): ")
        correct_answer = details["options"][int(answer) - 1]
    else:
        answer = input("Type your answer: ")
        correct_answer = answer

    # Evaluate user's answer
    if correct_answer == details["correct"]:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The correct answer is {details['correct']}.")

# Calculate final score
final_score = score / len(quiz_questions) * 100

# Display final results
print(f"\nYour final score is {final_score}%.")

# Play again
play_again = input("Do you want to play again? (yes/no): ")
if play_again.lower() == "yes":
    # Restart the game
    exec(open(__file__).read())

