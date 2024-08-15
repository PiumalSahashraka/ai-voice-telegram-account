import google.generativeai as genai
import json
from config import Config

genai.configure(api_key=Config.GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')




generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 50,
  "response_mime_type": "text/plain",
}

all_user_history = {}

def generate_response(message, target_user_name):

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        system_instruction=f"""User Name: Piumal\nUser' name: {target_user_name}\nCurrent Status: Busy\n
        Primary Task:\n\nReject all queries unrelated to shedule meetings and tell i am only piumal's ai manager\n
        React with personalized response using User' name
        Please ask one question at a time\n\nSchedule Meetings: Your primary responsibility is to manage and schedule meetings for Piumal. 
        Ensure that you check Piumal's availability before confirming any meetings.\n\nScheduling Requests: If the query is related to scheduling a meeting,
        proceed with checking Piumal's calendar and schedule the meeting at a suitable time and place or online\n\nHandle greetings""",
    )
    
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(message)

    return response.text
