import os 
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# LLM Configuration
def get_llm():
    return ChatGoogleGenerativeAI(
        model = "gemini-2.5-flash",
        google_api_key = os.getenv('GOOGLE_API_KEY'),
        temperature = 0,
    )

# Neo4j Configuration
def get_neo4j_config():
    return {
        'uri': os.getenv('NEO4J_URI'),
        'user': os.getenv('NEO4J_USERNAME'),
        'password': os.getenv('NEO4J_PASSWORD')
    }

