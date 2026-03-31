from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

client = OpenAI(
    api_key=os.getenv("SILICONFLOW_API_KEY"),
    base_url="https://api.siliconflow.cn/v1"
)

def analyze_resume(job_description, resume):
    prompt = f"""
你是一位专业的HR顾问，请分析以下简历与职位的匹配程度。

【职位描述】
{job_description}

【简历内容】
{resume}

请按以下格式输出：
1. 匹配度评分（0-100分）
2. 优势（简历中符合职位要求的部分）
3. 不足（简历中缺失的关键要求）
4. 改进建议（具体怎么修改简历）
5.推荐学习资源（如果有需要提升的技能，请推荐相关的学习资源）
"""

    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V3",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

print("=== 简历分析器 ===\n")
print("请输入职位描述（输入完成后按两次回车）：")

job_lines = []
while True:
    line = input()
    if line == "":
        break
    job_lines.append(line)
job_description = "\n".join(job_lines)

print("\n请输入简历内容（输入完成后按两次回车）：")
resume_lines = []
while True:
    line = input()
    if line == "":
        break
    resume_lines.append(line)
resume = "\n".join(resume_lines)

print("\n分析中...\n")
result = analyze_resume(job_description, resume)
print(result)