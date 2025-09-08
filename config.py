import os
from dotenv import load_dotenv

# Cargar .env solo si existe (desarrollo)
if os.path.exists(".env"):
    load_dotenv()   

# API Admin para amigocloud
PATH_OUTPUT_DATA = os.getenv('PATH_OUTPUT_DATA')
