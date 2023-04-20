import openai

openai.api_key = "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"

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
