import openai
import sys
import os
sys.path.append("../")
import GPT_Key as gpt #type: ignore
openai.api_key = gpt.key

# openai.api_key = "YOUR_API_KEY"

class ChatGPT:
    def __init__(self, role=None) -> None:
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
    
    def Loader(self, Log):
        self.Messages.append(Log)
    
    
    def Saving_Messages(self) -> None:
        title = "Please Provide a 3 Worded Title for this conversation. NOTE: Only 3 Words and should described what we talked about and don't end the words with '.'(Fullstop) not even inside Double Quotes or Single Quotes. NOTE (Carefully): Write the Title in this Format Your_Conversation_Title OR Conversation_With_You, etc"
        Title = self.ask(title)
        self.Messages.pop()
        self.Messages.pop()
        with open(f"{Title}.log", "a+") as log:
            log.write(str(self.Messages))
            log.close()
        os.system("move.bat")
        
    def Updating_Messages(self, filename):
        with open(filename, "w") as f:
            f.write(str(self.Messages))
            f.close()
        os.system("move.bat")