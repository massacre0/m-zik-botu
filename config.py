import os
API_ID = int(os.getenv("13100218"))
API_HASH = os.getenv("8f0fb4b161a3fdfc291b798572ad5ead")
BOT_TOKEN = os.getenv("5462358556:AAEpdEMSyko0EZya88wDRuJ8nPMuxY5eecs")
DATABASE_URL = os.getenv("DATABASE_URL")
OWNER_ID = list({int(x) for x in os.environ.get("5307220102", "1342133634").split()})