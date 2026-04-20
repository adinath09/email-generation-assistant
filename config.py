import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

MODEL_A = "llama-3.1-8b-instant"
MODEL_B = "llama-3.3-70b-versatile"