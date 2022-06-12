import sys
import logging
import importlib
from pathlib import Path

def load_plugins(plugin_name):
    path = Path(f"TgProtectronBot/plugins/{plugin_name}.py")
    name = "TgProtectronBot.plugins.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["NoinoiRobot.plugins." + plugin_name] = load
    print("𝙿𝙻𝚄𝙶𝙸𝙽 𝙰𝙳𝙳𝙴𝙳 𝚂𝚄𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 >> " + plugin_name)
