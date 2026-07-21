# 1. Define the quiz data using tuples (a tuple of tuples)
quiz = (
    ("Capital of India?", "Delhi"),
    ("5 + 5?", "10"),
    ("Python creator?", "Guido van Rossum")
)

# Initialize the score counter
score = 0

# 2. Iterate through each question and answer pair
for question, correct_answer in quiz:
    # Ask the question
    user_answer = input(f"{question} ")
    
    # Check the answer (case-insensitive for text flexibility)
    if user_answer.strip().lower() == correct_answer.lower():
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is: {correct_answer}\n")

# 3. Display the final score
total_questions = len(quiz)
print(f"Quiz Over! Your final score is {score}/{total_questions}.")