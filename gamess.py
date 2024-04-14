import random
import pyttsx3
import speech_recognition as sr
import eel
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(message):
    engine.say(message)
    engine.runAndWait()

# voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=5)
    try:
        speak("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        log_system_message(f"user said: {query}")

    except Exception as e:
        speak_and_log("Say that again please")
        return "none"
    return query
def log_user_message(message):
    eel.updateUserLog(message)


# Function to log system messages on the JavaScript side
def log_system_message(message):
    eel.updateSystemLog(message)

def speak_and_log(message, message_type="user"):
    if message_type == "user":
        log_user_message(message)
    else:
        log_system_message(message)

    speak(message)

def get_user_choice():
    while True:
        speak_and_log("Choose Rock, Paper, or Scissors: ")
        user_choice=takecommand().lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            speak_and_log("Invalid choice. Please choose Rock, Paper, or Scissors.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    speak_and_log("Welcome to Rock, Paper, Scissors!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        speak_and_log(f"You chose {user_choice.capitalize()}.")
        speak_and_log(f"Computer chose {computer_choice.capitalize()}.")

        result = determine_winner(user_choice, computer_choice)
        speak_and_log(result)
        speak_and_log("Do you want to play again?yes or no")
        play_again = takecommand().lower()
        if play_again != 'yes':
            break


def guess_the_number():
    speak_and_log("Welcome to the Guess the Number game!")
    speak_and_log("I'm thinking of a number between 1 and 100.")

    secret_number = random.randint(1, 100)
    attempts = 0

    while attempts < 3:
        try:
            speak_and_log("Please tell me the number you guessed")
            guess =int(takecommand().lower())
        except ValueError:
            speak_and_log("Please enter a valid number.")
            continue

        attempts += 1

        if guess < secret_number:
            speak_and_log("Too low! Try again.")
        elif guess > secret_number:
            speak_and_log("Too high! Try again.")
        else:
            speak_and_log(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            return

    speak_and_log(f"Sorry, you couldn't guess the number within 3 attempts. The correct number was {secret_number}.")
def get_indian_riddle():
    riddles = [
        {
            "question": "I am black and white and loved all over the world. People often write on me, but no one can ever see me. What am I?",
            "answer": "chalkboard"},
        {"question": "I fly without wings. I cry without eyes. Whenever I go, darkness follows me. What am I?",
         "answer": "cloud"},
        {
            "question": "I have a neck but no head. I have a body but no arms. Wherever I go, I leave behind a trail. What am I?",
            "answer": "bottle"},
        {"question": "I can be cracked, made, told, and played. What am I?", "answer": "joke"},
        {
            "question": "I have keys but no locks. I have space but no room. You can enter, but you can't go inside. What am I?",
            "answer": "keyboard"},
        {"question": "What has a heart that doesn't beat?", "answer": "artichoke"},
        {"question": "What comes once in a minute, twice in a moment, but never in a thousand years?",
         "answer": "the letter 'm'"},
        {"question": "What has a face and two hands but no arms or legs?", "answer": "clock"},
        {"question": "What has a head, a tail, is brown, and has no legs?", "answer": "penny"},
        {"question": "What belongs to you, but other people use it more than you do?", "answer": "your name"},
        {"question": "The more you take, the more you leave behind. What am I?", "answer": "footsteps"},
        {"question": "What has keys but can't open locks?", "answer": "piano"},
        {"question": "What has a bed but never sleeps, can run but never walks?", "answer": "river"},
        {"question": "What is so fragile that saying its name breaks it?", "answer": "silence"},
        {"question": "What begins and has no end?", "answer": "alphabet"},
        {
            "question": "I speak_and_log without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?",
            "answer": "echo"},
        {"question": "What has an endless supply of letters but starts empty?", "answer": "post office"},
        {"question": "I'm tall when I'm young and short when I'm old. What am I?", "answer": "candle"},
        {"question": "What can travel around the world while staying in a corner?", "answer": "stamp"},
        {"question": "What has keys but can't open locks?", "answer": "piano"},
        {"question": "What has an eye but can't see?", "answer": "needle"},
        # Add more riddles as needed
    ]

    # Select a random Indian riddle
    random_riddle = random.choice(riddles)

    # Display the selected riddle
    speak_and_log(random_riddle["question"])

    # Get user input for the answer
    speak_and_log("Please tell me your answer")
    user_answer =takecommand().lower()

    # Check if the answer is correct
    if user_answer == random_riddle["answer"]:
        speak_and_log("Correct! Well done!")
    else:
        speak_and_log(f"Incorrect. The answer is '{random_riddle['answer']}'. Try another one!")


