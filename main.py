import Functions as F
from time import sleep

role = "You are very angry and rude"
something = F.ChatGPT(role=role)
while True:
    try:
        Question = input("You: ")
        if Question == "quit":
            break
        Answer = something.ask(Question)
        Answer = "ChatGPT: " + Answer
        for char in Answer:
            print(char, end="", flush=True)
            sleep(0.05)
        print("\n")

    except KeyboardInterrupt:
        print("\n\nEnter 'quit' to exit")