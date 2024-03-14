#QUIZ GAME
# YT VIDEO LINK : https://youtu.be/NpmFbWO6HPU?si=DLQwM92QYvLZfbiT
import nltk
from nltk.metrics import edit_distance
tolerance = 2

def check_closest_match(user_answer, correct_answer):
    """
    Check if the user's answer is close enough to the correct answer within a given tolerance.
    
    Parameters:
    user_answer (str): The answer entered by the user.
    correct_answer (str): The correct answer.
    tolerance (int): The allowed Levenshtein distance between the user's answer and the correct answer.
    
    Returns:
    bool: True if the user's answer is close enough to the correct answer, False otherwise.
    """
    # Calculate Levenshtein distance between the user's answer and the correct answer
        # Check if the user wants to quit
    if user_answer.lower() in ['q', 'quit']:
        print("Quitting the game.")
        quit()


    distance = edit_distance(user_answer.lower(), correct_answer.lower())
    
    # Check if the distance is within the tolerance
    if distance <= tolerance:
        print("Close enough.")
        return True

    else:
        return False
    

print("QUIZ GAME")
print("Welcome to my Computer Quiz!")

playing = input("Do you wanna play the game, Press Enter to Start or press 'Q' to quit! ")

if playing.lower() == "q":
    quit()

print("Okay !Let's Play :) ")
score = 0

while True:
    answer = input("What does CPU stands for?\n")
    correct_answer = "central processing unit"

    
    if answer.lower() == correct_answer:
        print("Correct Answer !")
        score += 1
    else:
        if not check_closest_match(answer, correct_answer):
            print("Wrong Answer !")


    answer = input("What does GPU stands for?")
    correct_answer = "graphics processing unit"

    if answer.lower() == correct_answer:
        print("Correct Answer !")
        score += 1
    else:
        if not check_closest_match(answer, correct_answer):
            print("Wrong Answer !")
            choice = input("Press any key to try again! or press q to quit!")
            if choice.lower() == "q":
                quit()


    answer = input("What does RAM stands for?")
    correct_answer = "random access memory"
    if answer.lower() == correct_answer:
        print("Correct Answer !")
        score += 1
 
    else:
        if not check_closest_match(answer, correct_answer):
            print("Wrong Answer !")
            choice = input("Press any key to try again! or press q to quit!")
            if choice.lower() == "q":
                quit()


    answer = input("What does PSU stands for?")
    correct_answer = "power supply unit"

    if answer.lower() == correct_answer:
        print("Correct Answer !")
        score += 1
        break
    else:
        if not check_closest_match(answer, correct_answer):
            print("Wrong Answer !")
            choice = input("Press any key to try again! or press q to quit!")
            if choice.lower() == "q":
                break
            
print(f"You Finished the quiz, your final score is {score}")