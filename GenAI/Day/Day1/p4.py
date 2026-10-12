import os 
from dotenv import load_dotenv,detenv_values,find_dotenv


#loads .env form current directory 

load_dotenv()
config = dotenv_values(".env") # returns a dictionary of key-value pairs from .env file
api_key = config.get("GEMINI_API_KEY") # get the value of GEMINI_API_KEY key from .env file
api_key = os.getenv("GEMINI_API_KEY","") # get the value of GEMINI_API_KEY key from .env file
api_key = os.environ("GEMINI_API_KEY") # get the value of GEMINI_API_KEY key from .env file