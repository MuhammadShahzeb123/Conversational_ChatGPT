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
