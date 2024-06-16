import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
DB_PATH = './data/job_data.db'
driver_path = os.path.join(os.path.dirname(__file__), 'driver', 'chromedriver.exe')
