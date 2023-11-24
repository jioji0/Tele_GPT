from openai import OpenAI
client = OpenAI(
    api_key="apiKey"
)
import datetime

def Command(Prompt):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        temperature=0,
        messages=[
            {"role": "user", "content": Prompt}
        ]
    )
    result = completion.choices[0]
    message = result.message.content
    print(datetime.datetime.now())
    return message

print("test :", Command("너는 gpt가 맞지?"))

'''
completion = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[
        {"role": "system", "content": "You are poetic assistant, skilled an explaining"},
        #{"role": "user", "content": Prompt}
        {"role": "user", "content": "겨울에 대한 시를 써줘. json"}
    ],
    response_format={"type": "json_object"}
)

print(completion.choices[0].message.content)
'''
