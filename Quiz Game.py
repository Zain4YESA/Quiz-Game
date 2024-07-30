import pandas as pd
import matplotlib.pyplot as plt

#-----------------------------------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in question:
        print("-----------------------------------------------")
        print(key)
        print("-----------------------------------------------")
        for i in option[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(question.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)
    plot_results(guesses, correct_guesses)
#-----------------------------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("Correct:)")
        return 1
    else:
        print("Wrong:(")
        return 0
#-----------------------------------------------
def display_score(correct_guesses, guesses):
    print("-----------------------------------------------")
    print("Results")
    print("-----------------------------------------------")
    print("Answers: ", end="")
    for i in question:
        print(question.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()
    print(f"Your score is: S{(correct_guesses/len(question))*100}%")
#-----------------------------------------------
def plot_results(guesses, correct_guesses):
    total_questions = len(question)
    incorrect_guesses = total_questions - correct_guesses

    # Prepare data for plotting
    data = {
        'Result': ['Correct', 'Incorrect'],
        'Count': [correct_guesses, incorrect_guesses]
    }
    df = pd.DataFrame(data)

    # Plot the results
    fig, ax = plt.subplots()
    df.plot(kind='bar', x='Result', y='Count', ax=ax, legend=False, color=['green', 'red'])

    # Set plot labels and title
    ax.set_xlabel('Result')
    ax.set_ylabel('Count')
    ax.set_title('Quiz Results')

    # Show plot
    plt.tight_layout()
    plt.show()
#-----------------------------------------------
def play_again():
    response = input("Do u want to continue(Yes or No)?: ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
#-----------------------------------------------

question = {
    "Who created Python?": "A",
    "Who is the best footballer player in the world?": "C",
    "Who created Facebook?": "B",
    "Is Python easy to learn?": "C"
}

option = [["A. Guido van Rossum", "B. Lionel Messi", "C. Mark Zuckerberg", "D. None"],
          ["A. Guido van Rossum", "B. Mark Zuckerberg", "C. Lionel Messi", "D. None"],
          ["A. Lionel Messi", "B. Mark Zuckerberg", "C. Guido van Rossum", "D. None"],
          ["A. Maybe", "B. No", "C. Yes", "D. None"]]

new_game()

while play_again():
    new_game()

print("Bye!!!!, Thank you for playing:)")
