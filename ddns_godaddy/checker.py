from ddns_godaddy.cml import Opts
from ddns_godaddy.config import Config
from ddns_godaddy.sess import GoDaddySession
from time import sleep
from requests import Session
from json import dumps


class Checker:
    def __init__(self, opt: Opts, cfg: Config):
        self._opt = opt
        self._cfg = cfg

    def check(self):
        self._ses = GoDaddySession(self._cfg)
        self._nses = Session()
        cfg = self._cfg
        r = self._ses.get(f'/v1/domains/{cfg.domain}/records/A/{cfg.name}').json()  # noqa: E501
        if len(r) > 0:
            self._cur = r[0]
        while True:
            self.update()
            sleep(cfg.ttl)

    def update(self):
        try:
            r = self._nses.get("http://ip-api.com/json").json()['query']
            print(r)
            cur = getattr(self, '_cur', None)
            cfg = self._cfg
            if cur is None or cur['data'] != r:
                print(f'Try to update to {r}')
                d = [{'data': r, 'name': cfg.name, 'ttl': cfg.ttl, 'type': 'A'}]  # noqa: E501
                u = f'/v1/domains/{cfg.domain}/records/A/{cfg.name}'
                j = self._ses.put(u, dumps(d, ensure_ascii=False, separators=(',', ': '))).status_code  # noqa: E501
                if j == 200:
                    print(f'Update to {r} successfully.')
                    self._cur = d[0]
        except Exception:
            from traceback import print_exc
            print_exc()
