from openai import OpenAI
client = OpenAI(
    api_key="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"
)


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