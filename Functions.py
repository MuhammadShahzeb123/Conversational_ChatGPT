import openai
import sys
sys.path.append("../")
import ChatGPT as gpt

openai.api_key = gpt.key

# openai.api_key = "YOUR_API_KEY"

class ChatGPT:
    def __init__(self, role) -> str:
        self.Messages =  [
                {"role": "system", "content": role}       
            ]
    
    def ask(self, Q):
        self.Messages.append({"role": "user", "content": Q})
        
        responce = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=self.Messages
        )

        
        self.Messages.append({"role": "assistant", "content": responce["choices"][0]["message"]["content"]})

        return responce["choices"][0]["message"]["content"]
    
    def Saving_Messages(self) -> None:
        with open("Logs", "a") as log:
            for Message in self.Messages:
                log.write(Message)
            log.close()