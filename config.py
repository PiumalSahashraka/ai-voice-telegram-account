import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    API_ID = os.getenv('API_ID')
    API_HASH = os.getenv('API_HASH')
    PHONE_NUMBER = os.getenv('PHONE_NUMBER')
    DG_API_KEY = os.getenv('DG_API_KEY')