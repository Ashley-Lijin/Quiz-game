import json

# getting the data from json file
with open("data.json", "r") as quiz:
    data = json.load(quiz)

# for score
score = 0

# looping the json values
for key, value in data.items():
    print(value["question"])
    answer = input('Answer ? ')

    '''
    checking weather the answer is correct or wrong
    if answer is correct then the score will increase
    else the score is will be the same
    '''

    if answer.lower() == value["answer"].lower():
        score = score + 1
        print("correct :)  ")
        print('You score is: {} \n'.format(score))
    else:
        print("Wrong :(")
        print("The answer is : {} \n ".format(value["answer"]))
        print('You score is: {} \n'.format(score))

print('you got {} got 2 questions correctly'.format(score))
print('Your percentage is {} %'.format(score/2*100))