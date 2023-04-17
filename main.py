import json

# getting the data from json file
with open("data.json", "r") as quiz:
    data = json.load(quiz)

# for score
score = 0

# looping the json values
for key, value in data.items():
    # printing the question and asking the answer to user
    print('\n' +value["question"])
    answer = input('Answer ? ')

    '''
    checking weather the answer is correct or wrong
    if answer is correct then the score will increase
    else the score is will be the same
    '''

    if answer.lower() == value["answer"].lower():
        score = score + 1
        print("correct :)  ")
        print('You score is: {} '.format(score))
    else:
        print("Wrong :(")
        print("The answer is : {} ".format(value["answer"]))
        print('You score is: {}'.format(score))

# total number of question correct &  percentage

print('\nyou got {} got 2 questions correctly'.format(score))
print('Your percentage is {} %'.format(score/2*100))
