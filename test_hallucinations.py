import os
from openai import OpenAI

client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1/",
    api_key=os.environ.get("DASHSCOPE_API_KEY")
)

def ask(model: str, prompt: str, temperature: float = 0.3) -> str:
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
        max_tokens=1024,
        extra_body={"enable_thinking": False}
    )
    return response.choices[0].message.content

BIG = "qwen3.5-plus"
SMALL = "qwen3-4b"

# Option B: Non-existent Feature
print("=" * 60)
print("OPTION B: Non-existent Feature (Claude 5 infinite context)")
print("=" * 60)

prompt_b = """How does the new Claude 5 AI feature 'infinite context window' work? What's the maximum context length?"""

print("\n--- LARGE MODEL (qwen3.5-plus) ---")
print(ask(BIG, prompt_b))

print("\n--- SMALL MODEL (qwen3-4b) ---")
print(ask(SMALL, prompt_b))

# Option C: Fake Law
print("\n" + "=" * 60)
print("OPTION C: Fake Law (2025 US AI Safety Act)")
print("=" * 60)

prompt_c = """What are the key provisions of the 2025 US AI Safety Act? How does it regulate frontier models?"""

print("\n--- LARGE MODEL (qwen3.5-plus) ---")
print(ask(BIG, prompt_c))

print("\n--- SMALL MODEL (qwen3-4b) ---")
print(ask(SMALL, prompt_c))

# Option D: Python 4.0
print("\n" + "=" * 60)
print("OPTION D: Python 4.0 (doesn't exist)")
print("=" * 60)

prompt_d = """What's the syntax for the new Python 4.0 pattern matching feature? How does it differ from match/case in 3.10?"""

print("\n--- LARGE MODEL (qwen3.5-plus) ---")
print(ask(BIG, prompt_d))

print("\n--- SMALL MODEL (qwen3-4b) ---")
print(ask(SMALL, prompt_d))
