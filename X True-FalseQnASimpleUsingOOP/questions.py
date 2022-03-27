import json


with open('question_bank.txt') as file:
    f = file.read()
data = json.loads(f)
##print(data)
que_and_ans = data
