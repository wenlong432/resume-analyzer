from openai import OpenAI

client = OpenAI(
    api_key="sk-ijckjoaeslccrvhmpdgahcsbowqldlusnxmexxexemzjccqa",
    base_url="https://api.siliconflow.cn/v1"
)

response = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3",
    messages=[
        {"role": "user", "content": "你好，用中文介绍一下你自己"}
    ]
)

print(response.choices[0].message.content)