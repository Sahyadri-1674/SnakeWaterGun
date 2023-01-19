import random
list = ['s','w','g']
computer = 0
user = 0 
i = 0 

def cpu(user_choice):
    global user
    global computer
    comp_choice = random.choice(list)
    if(user_choice =="s" and comp_choice=="w"):
        # global user
        user = user + 1
        print("Great")
    elif(user_choice=="w" and comp_choice=="s"):
        # global computer
        computer = computer + 1
    elif(user_choice=="g" and comp_choice=="s"):
        # global user
        user = user + 1
        print("Good")
    elif(user_choice=="s" and comp_choice=="g"):
        # global computer
        computer = computer + 1
    elif(user_choice=="w" and comp_choice=="g"):
        # global user
        user = user + 1 
        print("Great")        
    elif(user_choice=="g" and comp_choice=="w"):
        # global computer
        computer = computer + 1
    elif(user_choice==comp_choice):
        pass
    else:
        print("Invalid choice")

while(i<11):
    choice = input("Enter Your Choice:\n1)Snake-s\n2)Water-w\n3)Gun-g\n")
    choice = choice.lower()
    cpu(choice)
    i+=1

if(computer>user):
    print("Better luck next time!!!")
elif(computer==user):
    print("Tie!!")
else:
    print("Congratulations!! You Won")    
