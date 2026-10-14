# Zero-shot = give the task directly, no examples. The model uses only what it learned during training.
from openai import OpenAI

#MODEL = "phi3:mini"    # 4 GB RAM
MODEL = "gemma2:2b"  # 8 GB RAM

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

prompt = """Classify the sentiment of this review as Positive, Negative, or Neutral.
Reply with one word only.

Review: "Ordered on 9th. Got it on 10th. With open box delivery. After opening neither charger not laptop switched on. Delivery guy repacked and took it back. I thought I will get replacement but later come to know that it has been cancelled by the delivery guys." """

r = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": prompt}],
    max_tokens=5,
    temperature=0.0,   # deterministic — classification should always give the same answer
)
print(r.choices[0].message.content.strip())