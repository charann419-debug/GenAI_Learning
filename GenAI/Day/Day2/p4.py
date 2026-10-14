# First API Call wrt Gemini
import google.generativeAI as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env 
load_dotenv()
genai.configure(api_key=os.getenv("GENAI_API_KEY"))

#Create a model instance with config
# 2.0, 2.5, 3.5
model = genai.GenerativeModel(model_name="gemini-3.8-flash",generation_config={"temperature":0.7,"max_output_tokens":150},system_instructions="You are a concise AI tutor. Answer in 2-3 sentences.")

#call the model
restult=model.generate_content("what is a vector database?")
print(result.text)
print(f"Tokens:{result.usage_metrics.total_output_tokens}")