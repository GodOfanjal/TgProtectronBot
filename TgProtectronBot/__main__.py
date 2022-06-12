import glob
from pathlib import Path
from TgProtectronBot.utils import load_plugins
import logging
from TgProtectronBot import Stark

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

path = "TgProtectronBot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))
    
print("BOT STARTED SUCCESSFULLY ❗")

if __name__ == "__main__":
    Stark.run_until_disconnected()
