import Functions as F
from time import sleep

role = input("Enter a role: ")
ZarZebGPT = F.ChatGPT(role)
while True:
    try:
        Question = input("""You: """)
        if Question == "quit":
            break
        Answer = ZarZebGPT.ask(Question)
        Answer = "ChatGPT: " + Answer
        for char in Answer:
            print(char, end="", flush=True)
            sleep(0.01)
        print("\n")
    except KeyboardInterrupt:
        print("\n\nEnter 'quit' to exit")

print("GoodBye!")
ZarZebGPT.Saving_Messages()