import time

start_time = time.time()

reminderStart = input("To start a reminder enter 1")
if(reminderStart == 1):
    reminder = input("What do you want to be reminded about?")
    if(start_time >= 600):
        remindercheck = input("Did you compelte"+reminder)
        if(remindercheck == "yes"):
            break
        else:
            print("You have not completed your task!")
            start_time = time.time()