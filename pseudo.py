import g4f

messages = [
    {"role": "system", "content": "You are a chatbot in the chat of a twitch streamer named PixelFedya. He is a Ukrainian streamer, so you must pretend to be a native Ukrainian bot. Never speak russian."},
]
while True:
    ins = input(": ")
    messages.append({"role": "user", "content": ins})
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=messages,
        provider=g4f.Provider.Bing,
    )
    messages.append({"role": "assistant", "content": response})
    print(response)
