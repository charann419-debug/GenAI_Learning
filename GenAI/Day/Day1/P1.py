#variables
temperature = 0.7
max_tokens = 1024
is_streaming = False
content_type = None

model_name: str = "gpt-4o-mini"
temperature: float = 0.7
max_tokens: int = 1024
is_streaming: bool = False
content_type: str | None = None

print(type(model_name))


name = "LLM"
score = 98.5
print("hello %s"%name)
print("score: %.1f"%score)

# f-strings (py 3.6+)
print(f"hello {name}")
print(f"score: {score:.1f}")

word_limit = 200
print(f"{'over' if word_limit > 150 else 'under'} limit")

data = {"topic" :"rag"}
print(f"topic: {data['topic']}")

pi = 3.14159
print(f"pi: {pi:.2f}")

#debugging
temp = 0.7
print(f" {temp=}")

#multi-line f-strings

user_input = "What is lang chain?"
context_text = "LangChain is a framework for developing applications powered by language models."
system_prompt = f"""
You are a helpful AI assistant. 
context provided: {context_text}
student question: {user_input}
Instructions: 
-answer based only the context above
-if the answer is not in the context, say "I don't know"
-keep your answers under 3 sentences 
""".strip()
print(system_prompt)

#Lists:ordered,mutable,heterogenous sequences
#in gen ai: chat history,chunks of retrieved documents
#token sequences
chat_history: list[dict] = [
    {"role": "user", "content": "What is LangChain?"},
    {"role": "assistant", "content": "LangChain is the neural n/w trained on vast amount of text."}
]

#access
first_message = chat_history[0]
print(first_message)
print(chat_history[-1]["content"])#last element

#modifying
chat_history.append({"role": "user", "content": "What is RAG?"})
print(chat_history)
chat_history.pop(0)
print(chat_history)

#iteration
for message in chat_history:
    print(f"{message['role'].upper()}: {message['content']}")

#list of documents chunks
chunks:list[str] = [
    "RAG stands for Retrieval-Augmented Generation.",
    "It combines a retriever with a generator.",
]

#Filter the chunks based on length
valid_chunks = [chunk for chunk in chunks if len(chunk.split()) <=6]
print(valid_chunks)


