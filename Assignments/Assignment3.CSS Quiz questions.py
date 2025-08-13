# CSS Quiz Game in Python

def run_quiz():
    print("Welcome to the CSS Quiz Game!\n")

    questions = [
        {
            "question": "1. What does CSS stand for?",
            "options": {
                "a": "Colorful Style Sheets",
                "b": "Cascading Style Sheets",
                "c": "Creative Style System",
                "d": "Computer Styling Syntax"
            },
            "answer": "b"
        },
        {
            "question": "2. Which property is used to change the text color in CSS?",
            "options": {
                "a": "text-color",
                "b": "font-color",
                "c": "color",
                "d": "text-style"
            },
            "answer": "c"
        },
        {
            "question": "3. Which symbol is used for ID selectors in CSS?",
            "options": {
                "a": ".",
                "b": "#",
                "c": "@",
                "d": "$"
            },
            "answer": "b"
        },
        {
            "question": "4. Which property is used to change the background color?",
            "options": {
                "a": "bgcolor",
                "b": "background-color",
                "c": "color-background",
                "d": "background"
            },
            "answer": "b"
        },
        {
            "question": "5. Which CSS property controls the size of text?",
            "options": {
                "a": "text-size",
                "b": "font-size",
                "c": "font-style",
                "d": "size"
            },
            "answer": "b"
        },
        {
            "question": "6. Which unit is NOT relative in CSS?",
            "options": {
                "a": "em",
                "b": "rem",
                "c": "px",
                "d": "%"
            },
            "answer": "c"
        },
        {
            "question": "7. Which property makes text bold in CSS?",
            "options": {
                "a": "font-weight",
                "b": "font-bold",
                "c": "text-weight",
                "d": "bold"
            },
            "answer": "a"
        },
        {
            "question": "8. Which value of position places an element relative to the browser window?",
            "options": {
                "a": "absolute",
                "b": "relative",
                "c": "fixed",
                "d": "sticky"
            },
            "answer": "c"
        },
        {
            "question": "9. What is the default position value of HTML elements in CSS?",
            "options": {
                "a": "absolute",
                "b": "static",
                "c": "relative",
                "d": "fixed"
            },
            "answer": "b"
        },
        {
            "question": "10. Which property is used to underline text?",
            "options": {
                "a": "text-decoration",
                "b": "underline",
                "c": "font-decoration",
                "d": "text-style"
            },
            "answer": "a"
        
        }
    ]

    score = 0
    for q in questions:
        print(q["question"])
        for key, value in q["options"].items():
            print(f"{key}) {value}")
        answer = input("Your answer (a/b/c/d): ").lower()
        if answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f" Wrong! The correct answer is '{q['answer']}'\n")

    print(f"Your Final Score: {score}/{len(questions)}")
    if score == len(questions):
        print("Perfect! You're a CSS master!")
    elif score >= 15:
        print("Great job! Keep practicing!")
    else:
        print("You can improve! Review CSS basics.")


# Run the game
run_quiz()

#OUPUT:
#Welcome to the CSS Quiz Game!

#1. What does CSS stand for?
#a) Colorful Style Sheets
#b) Cascading Style Sheets
#c) Creative Style System
#d) Computer Styling Syntax
#Your answer (a/b/c/d): b
#Correct!

#2. Which property is used to change the text color in CSS?
#a) text-color
#b) font-color
#c) color
#d) text-style
#Your answer (a/b/c/d): c
#Correct!

#3. Which symbol is used for ID selectors in CSS?
#a) .
#b) #
#c) @
#d) $
#Your answer (a/b/c/d): b
#Correct!

#4. Which property is used to change the background color?
#a) bgcolor
#b) background-color
#c) color-background
#d) background
#Your answer (a/b/c/d): b
#Correct!

#5. Which CSS property controls the size of text?
#a) text-size
#b) font-size
#c) font-style
#) size
#Your answer (a/b/c/d): b
#Correct!

#6. Which unit is NOT relative in CSS?
#a) em
#b) rem
#c) px
#d) %
#Your answer (a/b/c/d): c
#Correct!

#7. Which property makes text bold in CSS?
#a) font-weight
#b) font-bold
#c) text-weight
#d) bold
#Your answer (a/b/c/d): a
#Correct!

#8. Which value of position places an element relative to the browser window?
#a) absolute
#b) relative
#c) fixed
#d) sticky
#Your answer (a/b/c/d): c
#Correct!

#9. What is the default position value of HTML elements in CSS?
#a) absolute
#b) static
#c) relative
#d) fixed
#Your answer (a/b/c/d): b
#Correct!

#10. Which property is used to underline text?
#a) text-decoration
#b) underline
#c) font-decoration
#d) text-style
#Your answer (a/b/c/d): a
#Correct!

#Your Final Score: 10/10
#Perfect! You're a CSS master!'''





