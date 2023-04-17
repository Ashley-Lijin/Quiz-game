import json

with open("data.json", "r") as quiz:
    data = json.load(quiz)

print(data)


for key, value in data.items():
    print(value["question"])
    answer = input('Answer ? ')

    if answer.lower() == value["answer"].lower:
        print("correct :)")
    else:
        print("correct :)")
        print("The answer is : {}".format(value["answer"]))
