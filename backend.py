import cohere
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize Cohere Client
co = cohere.Client(os.getenv("COHERE_API_KEY"))

# Function to get response from Cohere
def get_text_output(input_text):
    response = co.chat(
        model="command-r-plus",
        message=input_text
    )
    return response.text