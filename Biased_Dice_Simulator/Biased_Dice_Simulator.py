import random  # Importing the random module to generate random numbers

# Asking the user if they want to roll the dice
user = input("Do you want to roll the dice? : ")

# Continue rolling the dice as long as the user says "yes"
while user == "yes":
    # Creating a biased list of numbers where 6 appears more frequently
    biased_towards_six = [1, 2, 3, 4, 5, 6, 6, 6, 6,6,6]  # 6 has a higher probability
    a = random.choice(biased_towards_six)  # Randomly select one number from the biased list

    # Display the dice face based on the number rolled
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
    user = input("do u want to roll the dice again?:")