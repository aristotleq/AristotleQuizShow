# Display title of quiz show in ASCII art
print(r"""
     
  ___   __ __  ____  _____      ____   ___   ____         __ __  ____  
 /   \ |  |  ||    ||     |    |    \ /   \ |    \       |  |  ||    \ 
|     ||  |  | |  | |__/  |    |  o  )     ||  o  )_____ |  |  ||  o  )
|  Q  ||  |  | |  | |   __|    |   _/|  O  ||   _/|     ||  |  ||   _/ 
|     ||  :  | |  | |  /  |    |  |  |     ||  |  |_____||  :  ||  |   
|     ||     | |  | |     |    |  |  |     ||  |         |     ||  |   
 \__,_| \__,_||____||_____|    |__|   \___/ |__|          \__,_||__|   

""")

# Quick into and rules of the game

userName = input("Hello! What is your first name: ")
print()
print()
print(f"Hello {userName}. Welcome to Quiz Pop-up!")
print()
print(f"{userName}, you must answer a few True or False questions.")
print("Please answer the question by entering the letter T or F.")
print(f"Ok, {userName}, let's start.")
print()
print()
# Questions stored in a tuple
questions = ("Q1. The moon is the only natural satellite orbiting planet Earth.", "Q2. The grass is red.", "Q3. The sky is blue.", "Q4. Mercury is the closest planet to the Sun.")

# Answer stored in a separate tuple
answers = ("T", "F", "T", "T")

userGuess = ""
guessRight = 0

numberOfQuestions = len(questions)

# Show the user the question
for index in range(numberOfQuestions):
  print(questions[index])
  print()

  # Re-prompt user if other values are entered
  while(userGuess != "T" and userGuess != "F"):
  # Get the answer from the user
  userGuess = input("Please enter 'T' for true or 'F' for false: ")
  print()
  
    # Counter for correct answers
    if(userGuess == answers[index]):
    guessRight += 1
      
  userGuess = ""
# Display how many questions correct out of total number of questions
print(f"You got {guessRight} out of {numberOfQuestions} correct!")
# Exit greeting
print(f"Thanks for playing, {userName}!")
