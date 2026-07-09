#Quiz made by Nat King.

score = 0

questions = [
    {
        "question": "1.How do you change file permissions so that: Owner can read and write, Group can read, and Others have no access?",
        "options": ["A. chmod 721", "B. chmod 640", "C. chmod 422", "D. chmod 755"],
        "answer": "B"
    },

    {
        "question": "2.How do you move example.txt to the testing folder?",
        "options": ["A. mv example.txt /Users/cits/Desktop/testing", "B. rm example.txt", "C. Ls -la", "D. mkdir testing"],
        "answer": "A"
    },

    {
        "question": "3.What is the element W?",
        "options": ["A. Uranium", "B. Tungsten", "C. Lead", "D. Stronium"],
        "answer": "B"
    }

]

print("=====Welcome to My Quiz=====\n")

for q in questions:
    print(q["question"])

    for option in q["options"]:
        print(option)
    
    response = input("Enter Your Answer (A, B, C, or D): ").strip().upper()

    if response == q["answer"]:
        print("Correct!\n")
        score +=1
    else:
        print("Incorrect...The correct answer was {q['answer']}.\n")

print("=" * 40)
print(f"Your Final Score is {score}/{len(questions)}")
