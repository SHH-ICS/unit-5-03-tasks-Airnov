# Create a program that will accept a multiple choice question, four answers, and the letter of correct answer. 
# This will be six lines, and then store the questions in the file questions.txt.

answer = input("When was the first known use of the word 'monkey'? A: 1523 B: 1498 C: 1948 or D: 1043: ")
if answer == "B":
    print("Correct!")
else:
    print(f"The answer is 'B', not {answer!r}")

question = "When was the first known use of the word 'monkey'? A: 1523 B: 1498 C: 1948 or D: 1043"

with open("questions.txt", "a") as f:
    f.write(question + "\n")
