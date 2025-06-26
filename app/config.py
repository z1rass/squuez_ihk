from dotenv import load_dotenv
import os

load_dotenv(override=True)
AZUBI_NUMMER = os.getenv("AZUBI_NUMMER")
AUSBILDER_MAIL = os.getenv("AUSBILDER_MAIL")
PASSWORD = os.getenv("PASSWORD")
MAIL = os.getenv("AZUBI_MAIL")
GEMINI_API_TOKEN = os.getenv("GEMINI_API_TOKEN")
WEB_UNTIS_USERNAME = os.getenv("WEB_UNTIS_USERNAME")
WEB_UNTIS_PASSWORD = os.getenv("WEB_UNTIS_PASSWORD")
WEB_UNTIS_MAIL = os.getenv("WEB_UNTIS_MAIL")
