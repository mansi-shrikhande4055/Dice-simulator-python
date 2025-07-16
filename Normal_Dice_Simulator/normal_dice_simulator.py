import random #to generate random numbers
user = input ("do u want to roll the dice?") # taking an input from user to proceed further.

while user== "yes":
    a = random.randint(1,6) #Return random integer in range [a, b], including both end points.
    if a==1:
        print ("---------")
        print ("|       |")
        print ("|   o   |")
        print ("|       |")
        print ("---------")
    if a==2:
        print ("---------")
        print ("| o     |")
        print ("|       |")
        print ("|     o |")
        print ("---------")
    if a==3:
        print ("---------")
        print ("| o     |")
        print ("|   o   |")
        print ("|     o |")
        print ("---------")
    if a==4:
        print ("---------")
        print ("| o   o |")
        print ("|       |")
        print ("| o   o |")
        print ("---------")
    if a==5:
        print ("---------")
        print ("| o   o |")
        print ("|   o   |")
        print ("| o   o |")
        print ("---------")
    if a==6:
        print ("---------")
        print ("| o   o |")
        print ("| o   o |")
        print ("| o   o |")
        print ("---------")
    user = input("do u want to roll the dice again?")