import google.generativeai as genai
import json
from config import Config

genai.configure(api_key=Config.GEMINI_API_KEY)

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
#   "max_output_tokens": 100,
  "response_mime_type": "text/plain",
}

all_user_history = {}

def generate_response(message, target_user_name):

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        system_instruction=f"User Name: {target_user_name}",
    )
    
    chat_session = model.start_chat(history=all_user_history.setdefault(target_user_name, []))
    response = chat_session.send_message(message)
    all_user_history[target_user_name].append(
        {
            "role": "user",
            "parts": [
                {"text": message} 
            ]
        }
    )
    all_user_history[target_user_name].append(
        {
            "role": "model",
            "parts": [
                {"text": response.text}  
            ]
        }
    )

    return response.text
