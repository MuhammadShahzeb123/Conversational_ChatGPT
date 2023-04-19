import openai

openai.api_key = "YOU_API_KEY"

class ChatGPT:
    def __init__(self, role) -> None:
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
