import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access the API key
api_key = os.getenv('LANGCHAIN_API_KEY')

# Print the API key to verify it's working
print(f"Your API Key is: {api_key}")
