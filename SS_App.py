#Vladislav Sereda
#Secret Santa App

#Imports
import random

#Global variables
participants = []
gifters = []
giftees = []
secret_santa = {}

#POPULATE command, see help()
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

#POOL command, see help()
def pool():
    global participants
    print("\nYou have the following people listed as participants: ")
    for i in participants:
        print(i, end = " ")
    print()

#ADD command, see help()
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

#REMOVE command, see help()
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

#ASSIGN command, see help()
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
        
#Hidden command that shows you the contents of the secret_santa dictionary
def peak():
    print(secret_santa)

#SHOW command, see help()
def show(gifter):
    giftee = secret_santa.get(gifter)
    txt = "{} is getting gifts for {}, they are {}'s secret Santa!"
    print(txt.format(gifter, giftee, giftee))

#HELP command
def help_prompt():
    print("""
The basic process for using this app is:
1. Use POPULATE to enter a list of participants for your secret Santa party.
2. Use ASSIGN command to assign everyone their secret Santa.
3. Have participants use the SHOW command to find out who they're getting gifts for.

- If you make any edits to the participant pool (POPULATE, ADD, REMOVE) *after* you've 
already used the ASSIGN command, you will have to run it again in order for your updates
to be reflected in the final outcome. 


These are the current commands (and their aliases, if applicable) that you can use:

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

def main():
    print("""
Welcome to my Secret Santa Test App!

I recommend using the HELP command to get a complete list of all commands 
available and their functions if you are not sure how to use this app.
""")
        
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

main()
