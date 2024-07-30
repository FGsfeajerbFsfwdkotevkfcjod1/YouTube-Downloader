import os

class Config:
    API_ID = int(os.getenv("API_ID", 28157070))
    API_HASH = os.getenv("API_HASH", '9078ae3b29412c4c1220e631edc5ed77')
    BOT_TOKEN = os.getenv("BOT_TOKEN", '7195643309:AAGGsnorpch1N8I1gMa_IYudiQzGQhkPEXk')
