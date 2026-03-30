from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)
CORS(app)

client = OpenAI(
    api_key="sk-ijckjoaeslccrvhmpdgahcsbowqldlusnxmexxexemzjccqa",
    base_url="https://api.siliconflow.cn/v1"
)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    job_description = data.get("job_description", "")
    resume = data.get("resume", "")

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
5. 推荐学习资源（针对不足之处推荐具体学习方向）
"""

    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V3",
        messages=[{"role": "user", "content": prompt}]
    )

    return jsonify({"result": response.choices[0].message.content})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)