# -*- coding: utf-8 -*-

"""
Knowledge competition
* Write a knowledge competition program
* It should consist of 10 questions in total
* Each question will have only one answer
* Adjust the answers of the questions according to case sensitivity
* Each question shoul be worth 10 points
* If user answers 5 or fewer questions, it will be considered unsuccessful
* If the user answers more than 5 questions correctly, it will be considered successful
"""

#%% İngilizce sorular
count = 0
questions = {"What is the hottest continent on Earth?": "Africa",
             "What is restricted by the ozone layer?":"Ultraviolet radiation",
             "Who was Euclid?": "Greek mathematician",
             "What is the longest river in the world?": "River Nile",
             "What are the five colours of the Olympic rings?":"Blue, yellow, black, green and red",
             "Which nuts are used in marzipan?":"Almonds",
             "Who is the only musician ever to have been awarded the Nobel prize for literature?":"Bob Dylan",
             "Which singer was known amongst other things as 'The King of Pop'?":"Michael Jackson",
             "Which club won the 2017 UEFA Super Cup?":"Real Madrid",
             "Which singer has the most UK Number One singles ever?":"Elvis Presley"}

for key, value in questions.items():
    print(key)
    cevap = input("your answer: ")
    if cevap == value:
        count += 1
        print("correct answer\n")
    else:
        print("wrong answer\n")

if count > 5:
    print("You have answered %d questions correctly, you won Congrats! :)" % count)
else:
    print("You have answered only %d questions correctly, this is not enough to win, you failed :(" % count)


