"""
Day 7：確認 API key 同環境設定正確

用法：
    python hello_claude.py
"""
import anthropic
from dotenv import load_dotenv

load_dotenv()  # 從 .env 讀取 ANTHROPIC_API_KEY

client = anthropic.Anthropic()
MODEL = "claude-haiku-5-5"  # 最平嘅 model，用嚟測試啱啱好

response = client.messages.create(
    model=MODEL,
    max_tokens=100,
    messages=[{"role": "user", "content": "Say hello in one short sentence."}],
)

print(response.content[0].text)
print(f"輸入 {response.usage.input_tokens} token，輸出 {response.usage.output_tokens} token")
