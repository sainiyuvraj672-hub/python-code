# quiz!!
questions = (("how many elements are in preodic table?"),
             ("which animal gives the biggest egg?"),
             ("what is most popular language in the world?"),
             ("what is the full form of nlp?"),
             ("when th python invent?"))

options = (("A. 118","B. 114","C. 205","D.116"),
         ("A. Cow", "B. Ostrich", "C. pegion", "D. Emu"),
        ("A. hindi","B. English","C. French","D. Espanol"),
        ("A. Natural Language Processing", "B. Neural Language Processing", "C, Network Language Processing", "D.Network Linguistic Processing"),
        ("A. 1991", "B. 1989", "C. 1990", "D. 1992"))

answers = ( "A","B","B","B","A")

guesses = []
score = 0
questions_num = 0

for question  in questions:
    print("------------------------")
    print(question)
    
    for option in options [questions_num]:
        print(option)
        
    guess = input("Enter your answer: ").upper()
    guesses.append(guess)
    if guess == answers[questions_num]:
        print("Correct answer!!")
        score += 1
    else:
        print("Incorrect answer!!")
        print(f"The correct answer is {answers[questions_num]}")
    questions_num +=1

    print(f"the current score is {score} out of {len(questions)}")

