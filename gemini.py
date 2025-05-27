import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
def ask_gemini(prompt: str) -> str:
    
    model = genai.GenerativeModel("models/gemini-2.5-flash-preview-04-17")
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating response from Gemini: {e}"