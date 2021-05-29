"""Bora Eskicioğlu-Global AI HUB-Final Project"""
import random
import time
print("Welcome to the Final Gaming Quiz !")
time.sleep(1)
print("In this Test, we are going to test your gaming knowledge by asking you total of 10 questions !")
time.sleep(1)
print("If you manage to answer more than 5 questions correctly you win !")
time.sleep(1)
print("If you can't you lose!")
time.sleep(1)
print("Let's begin !")
time.sleep(1)
counter=0
answers=["Luigi","Cloud","2020","Pong","Minecraft","Butterflies","Jump Man","Warthog","Mr. Needlemouse","Clank"]
questions=["What is the name of Mario's brother?","What is the name of the main character in Final Fantasy 7?",
           "When was the Playstation 5 released? (Year)","What was the first commercially successful video game?"
           ,"What is the best-selling video game of all time?","What inspired games maker Satoshi Tajiri to create Pokémon?",
           "What was Mario's original name?","What is the armoured vehicle in Halo called?",
           "What was Sonic the Hedgehog's original name?","What is the name of Ratchet’s killer robot friend?"
]
for i in range(10):
    if len(questions)==0:
        print("Game Over")
        break
    print((i+1),". question:")
    a=random.choice(questions)
    ans=input(a)
    for i in range(len(questions)):
        if a==questions[i] and ans==answers[i]:
            counter=counter+1
            break
    answers.pop(questions.index(a))
    questions.remove(a)
print("Let'see how much points you get !")
time.sleep(1)
print("You get",counter," points !")
time.sleep(1)
if counter >5:
    print("Congrats ! You win !")
else:
    print("Sorry,you lose. Better luck next time !")







