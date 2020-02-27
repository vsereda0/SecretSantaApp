#Vladislav Sereda
#Secret Santa App

#Imports
import random

#Global variables
participants = []
givers = []
recipients = []
secret_santa = {}

#POPULATE command, see help_prompt()
def populate():
    global participants, secret_santa, givers, recipients

    participants.clear()
    secret_santa.clear()

    try:
        count = int(input("\nPlease enter the number of participants: "))
    except ValueError:
        print("Enter a valid integer.")
        count = int(input("\nPlease enter the number of participants: "))

    for i in range(count):
        txt = "Please enter the name of participant #{}: "
        participant = str(input(txt.format(i + 1)))
        if participant.lower() == "exit":
            break
        else:
            participants.append(participant)

    assign()
    pool()

#POOL command, see help_prompt()
def pool():
    global participants
    print("\nYou have the following people listed as participants: ")
    for i in participants:
        print(i, end = " ")
    print()

#ADD command, see help_prompt()
def add(name):
    global participants
    
    if name not in participants:
        participants.append(name)
        assign()
        txt = "You have added {} to the list of participants."
        print(txt.format(name))
    else:
        txt = "{} is already on the list (no duplicate names allowed)."
        print(txt.format(name))

#RM command, see help_prompt()
def remove(name):
    global participants, secret_santa
    
    if name in participants:
        participants.remove(name)
        secret_santa.clear()
        assign()
        txt = "You have removed {} from the list of participants."
        print(txt.format(name))
    else:
        txt = "You couldn't remove {} because they were not in the list."
        print(txt.format(name))

#ASSIGN command, see help_prompt()
def assign():
    global participants, secret_santa, givers, recipients
    
    givers = participants.copy()
    recipients = participants.copy()

    while True:
        if len(givers) > 0:
            giver = random.choice(givers)
            recipient = random.choice(recipients)

            if giver != recipient:
                secret_santa[giver] = recipient
                givers.remove(giver)
                recipients.remove(recipient)
            else:
                assign()
        else:
            break
        
#Hidden command that shows you the contents of the secret_santa dictionary
def peak():
    print(secret_santa)

#SHOW command, see help_prompt()
def show(giver):
    recipient = secret_santa.get(giver)
    txt = "{} is getting gifts for {}, they are {}'s secret Santa!"
    print(txt.format(giver, recipient, recipient))

#XP command, see help_prompt()
def export(giver):
    recipient = secret_santa.get(giver)
    txt = "Hi {}, you will be buying gifts for {}!"
    
    ss_file = open(giver, "w")
    ss_file.write(txt.format(giver, recipient))
    ss_file.close()

#ALL option for the XP command, see help_prompt()
def export_all():
    txt = "Hi {}, you will be buying gifts for {}!"
    
    for giver, recipient in secret_santa.items():
        recipient = secret_santa.get(giver)
        ss_file = open(giver, "w")
        ss_file.write(txt.format(giver, recipient))
        ss_file.close()

#HELP command
def help_prompt():
    print("""
The recommended process for using this app is:
1. Use POPULATE to enter a list of participants for your secret Santa party.
2. Use XP ALL to create an output file for each participant that will tell them who
    they're buying gifts for.


These are the current commands (and their aliases, if applicable) that you can use:

POPULATE        (POP)   - Will prompt you to enter all the info to populate your secret Santa pool.
                             - This command overwrites all previous information entered.
                             - Enter "QUIT" if you would like to go back to the command line during
                             the process.
POOL            (PL)    - Will allow you to see who is currently in your secret Santa pool.
ADD [name]              - Will allow you to add an individual to your secret Santa pool.
RM [name]               - Will allow you to remove an individual from your secret Santa pool.
SHOW [name]             - Will show who the indicated participant is getting gifts for.
XP [all, name]          - Will export the secret Santa assignment(s) based on the option used.
                            - Using "XP ALL" will create output files for every participant.
                            - Using XP [name] will create a single output file for one giver.
HELP            (H)     - Will show you this prompt in case you forget the commands.
QUIT                    - Will end the application.
""")

def main():
    print("""
Welcome to my Secret Santa App!
I recommend using the HELP command to get a complete list of all commands 
available and their functions if you are not sure how to use this app.
""")
        
    while True:
        command = input("\n> ")
        if command.lower() == "populate" or command.lower() == "pop":
            populate()
        elif command.lower() == "pool" or command.lower() == "pl":
            pool()
        elif command.lower().startswith("add "):
            name = command[4:]
            add(name)
        elif command.lower().startswith("rm "):
            name = command[3:]
            remove(name)
        elif command.lower() == "peak":
            peak()
        elif command.lower().startswith("show "):
            name = command[5:]
            show(name)
        elif command.lower().startswith("xp "):
            if command.lower() == "xp all":
                export_all()
            else:
                name = command[3:]
                export(name)
        elif command.lower() == "help" or command.lower() == "h":
            help_prompt()
        elif command.lower() == "quit":
            break
        else:
            continue

main()
