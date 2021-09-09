from platform import system
from getopt import getopt, GetoptError
from typing import List
if system() == "Windows":
    import os
    DEFAULT_CONFIG = f'{os.environ["APPDATA"]}\\ddns-godaddy.yaml'
else:
    DEFAULT_CONFIG = "/etc/ddns-godaddy.yaml"


class Opts:
    config_file: str = DEFAULT_CONFIG

    def __init__(self, cml: List[str]):
        try:
            r = getopt(cml, 'hc:', ['help', 'config='])
            for i in r[0]:
                if i[0] == '-h' or i[0] == '--help':
                    self.print_help()
                    import sys
                    sys.exit(0)
                elif i[0] == '-c' or i[0] == '--config':
                    self.config_file = i[1]
        except GetoptError:
            from traceback import print_exc
            print_exc()
            import sys
            sys.exit(-1)

    def print_help(self):
        print('''ddns-backuper [options]
Options:
    -h, --help          Print help message.
    -c, --config <path> Set config file.''')
