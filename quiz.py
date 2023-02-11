quiz = {
    "Question1":{
        "question":"What is the capital of Karnataka?",
        "answer":"Bengaluru"
    },
    "Question2":{
        "question":"What is the capital of Tamil Nadu?",
        "answer":"Chennai"
    },
    "Question3":{
        "question":"What is the capital of Kerala?",
        "answer":"Tiruvanantapuram"
    },
    "Question4":{
        "question":"What is the capital of Andra Pradesh?",
        "answer":"Amaravathi"
    },
    "Question5":{
        "question":"What is the capital of Telangana?",
        "answer":"Hyderabad"
    },
}

score = 0

for key, value in quiz.items():
    print(value["question"])
    answer = input("Enter the answer = ")

    if answer.lower() == value["answer"].lower():
        print("You're answer is correct ")
        score += 1
        print("You're score is ",score)

    else:
        print("You're answer is wrong. The correct answer is = ", value["answer"])
        print("You're score is ",score)

percent = ((score/5)*100)
print("You're final score is", score, "With a percentage of ", percent,"%")
