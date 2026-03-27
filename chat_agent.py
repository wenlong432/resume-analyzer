from openai import OpenAI

client = OpenAI(
    api_key="sk-ijckjoaeslccrvhmpdgahcsbowqldlusnxmexxexemzjccqa",
    base_url="https://api.siliconflow.cn/v1"
)

messages = []

while True:
    user_input = input("你：")

    if user_input == "quit":
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V3",
        messages=messages
    )

    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})

    print(f"AI：{reply}\n")