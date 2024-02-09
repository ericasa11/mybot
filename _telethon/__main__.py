import asyncio
import sys
import glob
import logging
import importlib
from pathlib import Path
from telethon import TelegramClient, events
# from _telethon import app, xub, LOGGER
from _telethon import clients, ids, LOGGER, LOG_CHAT, start_bot
from _telethon.modules import *

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

print("[Task_1] : Prefer to load plugins Telethon")
def load_plugins(plugin_name):
    print(f"[Task_2] : load plugins {plugin_name} Telethon...")
    path = Path(f"_telethon/modules/{plugin_name}.py")
    name = "_telethon.modules.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["_telethon.modules." + plugin_name] = load
    print("[Task_3] : load_plugins() is done!")


print("[Task_4] : loading all modules...")
path = "_telethon/modules/*.py"
files = glob.glob(path)
for name in files:
    print("[Task_5] : looping modules...")
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))
        print("[Task_6] : loading plugin_name module...")

# app.start()
# print("Telethon User Client 1 Started ")
# app.run_until_disconnected
# xub.start()
# print("Telethon User Client 2 Started")
# xub.run_until_disconnected()


# async def start_bot():

#     for xo, cli in enumerate(clients):
#         try:
#             await cli.start()
#             ex = await cli.get_me()
#             # await join(cli)
#             print(f"Started as : [{ex.first_name}] 🔥")
#             await cli.send_message(LOG_CHAT, f"<code>hello dev, I'm client_{xo+1} is alive!!!</code>", parse_mode="html")
#             ids.append(ex.id)
#         except Exception as e:
#             print(f"#LOG : this session invalid\n")
#             logging.error(e, exc_info=True)
#             # print(f"{e}")
#             pass
            
    # await idle()

# print(f"#TASK_1 : starting function of start_bot()...")
# loop = asyncio.get_event_loop()
# # loop.run_until_complete(start_bot())
# loop.run_until_disconnected(start_bot())
# print(f"#TASK_2 : finish function of start_bot()...")

if __name__ == "__main__":
    print(f"#TASK_1 : starting function of start_bot()...")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_bot())

    # run_until_disconnected(start_bot())
    # loop.run_until_disconnected(start_bot())
    print(f"#TASK_2 : finish function of start_bot()...")
