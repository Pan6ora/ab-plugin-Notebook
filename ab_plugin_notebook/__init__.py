import subprocess
import pkg_resources
import brightway2 as bw
from re import search
from time import sleep
import activity_browser as ab
import os

from .layouts.tabs import RightTab

class Plugin(ab.Plugin):

    def __init__(self):
        infos = {
            'name': "Notebook",
        }
        ab.Plugin.__init__(self, infos)
        self.server = None

    def load(self):
        if self.server:
            self.server_kill()
        files_path = bw.projects.request_directory(f"plugins/ab_plugin_notebook/files")
        config_path = pkg_resources.resource_filename(__name__, 'jupyter_config')
        current_env = os.environ.copy()
        current_env["JUPYTER_CONFIG_DIR"] = config_path
        
        self.server = subprocess.Popen([
                        "jupyter","notebook",
                        f"--notebook-dir={files_path}"],
                        env=current_env,
                        stdin=None)
        sleep(2)

        self.rightTab = RightTab(self)
        self.tabs = [self.rightTab]

    def close(self):
        self.server_kill()

    def remove(self):
        self.server_kill()

    def server_kill(self):
        try:
            self.server.kill()
        except:
            print("Plugin-Notebook: server not running")
            pass