import subprocess
import brightway2 as bw
from re import search
from time import sleep
import activity_browser as ab
import os

from .layouts.tabs import LeftTab, RightTab
from .metadata import infos

class Plugin(ab.Plugin):

    def __init__(self):
        ab.Plugin.__init__(self, infos)
        self.server = None

    def load(self):
        files_path = bw.projects.request_directory(f"plugins/{infos['name']}/files")
        config_path = f"{ab.settings.ab_settings.plugins_dir}/Notebook/includes/jupyter_config"

        self.server = subprocess.Popen([
                        "env", f"JUPYTER_CONFIG_DIR={config_path}",
                        "jupyter","notebook",
                        f"--notebook-dir={files_path}"],
                        stdin=None)
        sleep(2)

        self.rightTab = RightTab(self)
        self.leftTab = LeftTab(self)
        self.tabs = [self.rightTab, self.leftTab]

    def close(self):
        self.server_kill()

    def remove(self):
        self.server_kill()

    def delete(self):
        self.server_kill()

    def server_kill(self):
        try:
            self.server.kill()
        except:
            print("Plugin-Notebook: server not running")
            pass