#Vladislav Sereda
#Secret Santa App

import random

participants = []
gifters = []
giftees = []
secret_santa = {}
        
def populate():
    global participants
    participants.clear()

    try:
        count = int(input("\nPlease enter the number of participants: "))
    except ValueError:
        print("Enter a valid integer.")
        count = int(input("\nPlease enter the number of participants: "))

    for i in range(count):
        txt = "Please enter the name of participant #{}: "
        participant = str(input(txt.format(i + 1)))
        participants.append(participant)

    print("\nYou have the following people listed as participants: ")
    for i in participants:
        print(i, end = " ")
    print()


def pool():
    global participants
    print("\nYou have the following people listed as participants: ")
    for i in participants:
        print(i, end = " ")
    print()

def add():
    global participants
    add_participant = str(input("Please enter the name to be added: "))
    if add_participant not in participants:
        participants.append(add_participant)
        txt = "You have added {} to the list of participants."
        print(txt.format(add_participant))
    else:
        txt = "{} is already on the list (no duplicate names allowed)."
        print(txt.format(add_participant))

def remove():
    global participants
    rm_participant = str(input("Please enter the name to be removed: "))
    if rm_participant in participants:
        participants.remove(rm_participant)
        txt = "You have removed {} from the list of participants."
        print(txt.format(rm_participant))
    else:
        txt = "You couldn't remove {} because they were not in the list."
        print(txt.format(rm_participant))

def assign():
    global participants, secret_santa, gifters, giftees
    
    gifters = participants.copy()
    giftees = participants.copy()

    while True:
        if len(gifters) > 0:
            gifter = random.choice(gifters)
            giftee = random.choice(giftees)

            if gifter != giftee:
                secret_santa[gifter] = giftee
                gifters.remove(gifter)
                giftees.remove(giftee)
            else:
                assign()
        else:
            break

def peak():
    print(secret_santa)

def show(gifter):
    giftee = secret_santa.get(gifter)
    txt = "{} is getting gifts for {}, they are {}'s secret Santa!"
    print(txt.format(gifter, giftee, giftee))

    

def help_prompt():
    print("""
These are the current commands in this app that you can use:

POPULATE     (POP)   - Will prompt you to enter all the info for your secret Santa pool.
                         - This command overwrites all previous information entered.
POOL         (PL)    - Will allow you to see who is currently in your secret Santa pool.
ADD                  - Will allow you to add an individual to your secret Santa pool.
REMOVE       (RM)    - Will allow you to remove an individual from your secret Santa pool.
ASSIGN       (SS)    - Will process your list of participants and assign everyone a secret Santa.
SHOW [name]          - Will show who the indicated participant is getting gifts for.
                         - The [name] option is mandatory.
HELP         (H)     - Will show you this prompt in case you forget the commands.
QUIT                 - Will end the application.
""")

def command_line():
    while True:
        command = input("\n> ")
        if command.lower() == "populate" or command.lower() == "pop":
            populate()
        elif command.lower() == "pool" or command.lower() == "pl":
            pool()
        elif command.lower() == "add":
            add()
        elif command.lower() == "remove" or command.lower() == "rm":
            remove()
        elif command.lower() == "assign" or command.lower() == "ss":
            assign()
        elif command.lower() == "peak":
            peak()
        elif command.lower().startswith("show "):
            name = command[5:]
            show(name)
        elif command.lower() == "help" or command.lower() == "h":
            help_prompt()
        elif command.lower() == "quit":
            break
        else:
            continue

def main():

    print("""
Welcome to my Secret Santa Test App!

I recommend you begin by using the POPULATE command to create your list of
Secret Santa participants. Use it again if you would like to start from scratch,
or use the ADD or REMOVE commands if you just want to make small edits to your
list. When you're ready, use the ASSIGN command to assign everyone a secret Santa.

Use the HELP command to get a complete list of all commands available and their functions!
""")
    
    command_line()


main()
