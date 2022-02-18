import os
from dotenv import load_dotenv

load_dotenv()

max_quality = int(os.getenv('MAX_QUALITY'))
