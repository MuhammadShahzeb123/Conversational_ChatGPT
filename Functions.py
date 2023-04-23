import openai
import sys
import os
sys.path.append("../")
import ChatGPT as gpt

openai.api_key = gpt.key

# openai.api_key = "YOUR_API_KEY"

class ChatGPT:
    def __init__(self, role) -> None:
        self.Messages =  [
                {"role": "system", "content": role}       
            ]
    
    def ask(self, Q: str) -> str:
        self.Messages.append({"role": "user", "content": Q})
        
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=self.Messages
        )

        
        self.Messages.append({"role": "assistant", "content": response["choices"][0]["message"]["content"]})

        return response["choices"][0]["message"]["content"]
    
    def Saving_Messages(self) -> None:
        title = "Please Provide a 3 Worded Title for this conversation. NOTE: Only 3 Words and should described what we talked about and don't end the words with '.'(Fullstop)"
        Title = self.ask(title)
        with open(f"{Title}.log", "x+") as log:
            for Message in self.Messages:
                log.write(str(f"{Message}\n"))
            log.close()
        os.system("move *.log logs")