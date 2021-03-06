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
    print("πΏπ»ππΆπΈπ½ π°π³π³π΄π³ πππ²π΄πππ΅ππ»π»π >> " + plugin_name)
