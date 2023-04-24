from Functions import ChatGPT
from time import sleep
import os

Logs = os.listdir("./logs")
for index, log in enumerate(Logs):
    print(f"{index}. {log}")

choice = input("Please Select a Conversation or enter `new` to start a new Chat: ")
new_bool = True

if choice == "new" or choice == "": 
    new_bool = True
    Role = input("Enter a role: ")
    ZarZebGPT = ChatGPT(role=Role)


elif int(choice) in range(len(Logs)):
    new_bool = False
    with open(f"./logs/{Logs[int(choice)]}", "r") as l:
        log_text = l.read()
        log_text2 = eval(log_text)
    ZarZebGPT = ChatGPT()
    ZarZebGPT.Messages = list(log_text2)

else:
    print("Invalid choice. Please try again.")
    exit()

while True:
    try:
        Question = input("""You: """)
        if Question == "q":
            break
        Answer = ZarZebGPT.ask(Question)
        Answer = "ChatGPT: " + Answer
        for char in Answer:
            print(char, end="", flush=True)
            sleep(0.01)
        print("\n")
        print("-----------------------------------------------------------------------------------------")
    except KeyboardInterrupt or ConnectionError:
        print("\n\nPlease try again Later or user `q` to quit.")
print("GoodBye!")

if new_bool == True:
    ZarZebGPT.Saving_Messages()
    
else:
    ZarZebGPT.Updating_Messages(Logs[int(choice)])