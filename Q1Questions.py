# Create a program that will accept a multiple choice question, four answers, and the letter of correct answer. 
# This will be six lines, and then store the questions in the file questions.txt.
import json

def store_question(question, options, correct_answer):
    with open("questions.txt", "w+") as f:
        content = f.read()
        CAdd = f"{question}\n{json.dumps(options)}\n{correct_answer}"
        f.write(f"{content}{CAdd}\n")

        """
        f.write(f"{question}n")
        f.write(f"{'n'.join(options)}n")
        f.write(f"{correct_answer}n")
        f.write("n")
        """

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

question1 = input("Question: ")
options1 = [input("1: "), input("2: "), input("3: "), input("4: ")]
correct_answer1 = input("answer: ")
store_question(question1, options1, correct_answer1)





