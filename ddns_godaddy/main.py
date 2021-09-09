from ddns_godaddy.cml import Opts
from ddns_godaddy.config import Config
from ddns_godaddy.checker import Checker

def main(cm=None):
    if cm is None:
        import sys
        cm = sys.argv[1:]
    cml = Opts(cm)
    cfg = Config(cml.config_file)
    chk = Checker(cml, cfg)
    chk.check()
