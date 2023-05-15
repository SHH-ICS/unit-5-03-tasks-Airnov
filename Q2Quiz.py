# Create a second program that will read the file questions.txt, formatted as described above, and pose the questions to the user. 
# The program will keep score of the number of questions answered correctly.
import json

ques = ""
ans = []
cor = 0
with open("questions.txt", "r") as f:
    row = 0
    for line in f.read().splitlines():
        row += 1
        if row == 1:
            ques = line
        elif row == 2:
            ans = json.loads(line)
        elif row == 3:
            cor = int(line)

i = 0
print(ques)
for an in ans:
    i+=1
    print(f"{i}) {an}")
input("Correct: ")

user_answer = int(input("Enter the correct option number: "))
if user_answer == cor:
    print("Correct")


