import openai


openai.api_key = "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"

def ask():
    responce = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"},
            {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
            {"role": "user", "content": "Where was it played?"}
        ]
    )

    return responce["choices"][0]["message"]["content"]
