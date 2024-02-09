import time
from datetime import datetime
import logging
from telethon import TelegramClient, events
from telethon.sessions import StringSession
# from config import *
# from config import API_ID, API_HASH



logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

LOGGER = logging.getLogger(__name__)
StartTime = time.time()
# app = TelegramClient(StringSession(TE_SESSION), api_id=API_ID, api_hash=API_HASH)
# xub = TelegramClient(StringSession(X_SESSION) api_id=API_ID, api_hash=API_HASH)

clients = []
ids = []

API_ID=9
API_HASH="e234"
LOG_CHAT=-1002

te_session_strings = [
    "string1",
    "string2",
    ]

if te_session_strings:
    for i, session_string in enumerate(te_session_strings):
        client_name = f"client{i+1}"
        print(f"{client_name}: Found.. Starting..📳")
        client = TelegramClient(StringSession(session_string),
            api_id=API_ID,
            api_hash=API_HASH,
            )
        
        clients.append(client)


async def start_bot():

    for xo, cli in enumerate(clients):
        try:
            await cli.start()
            ex = await cli.get_me()
            # await join(cli)
            print(f"Started as : [{ex.first_name}] 🔥")
            await cli.send_message(LOG_CHAT, f"<code>hello dev, I'm client_{xo+1} is alive!!!</code>", parse_mode="html")
            ids.append(ex.id)
        except Exception as e:
            print(f"#LOG : this session invalid\n")
            logging.error(e, exc_info=True)
            # print(f"{e}")
            pass
