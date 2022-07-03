__version__ = "1.0.1"
from ddns_godaddy.main import main


def start():
    import sys
    try:
        sys.exit(main())
    except Exception:
        from traceback import print_exc
        print_exc()
        sys.exit(-1)
