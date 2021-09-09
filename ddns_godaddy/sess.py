from requests import Session
from ddns_godaddy.config import Config
from urllib.parse import urlparse, ParseResult, urlunparse


class GoDaddySession(Session):
    def __init__(self, cfg: Config):
        Session.__init__(self)
        self._cfg = cfg
        self.headers.update({"accept": "application/json", "Authorization":
                             f"sso-key {cfg.key}:{cfg.secret}"})

    def deal_url(self, url):
        r = urlparse(url)
        if r.netloc == '':
            ll = list(r)
            ll[1] = f'api.{"ote" if self._cfg.ote else ""}godaddy.com'
            if ll[0] == '':
                ll[0] = 'https'
            r = ParseResult(*ll)
            url = urlunparse(r)
        return url

    def get(self, url, **kwargs):
        return Session.get(self, self.deal_url(url), **kwargs)

    def put(self, url, data, **kwargs):
        head = kwargs.get("headers")
        if head is None:
            head = {}
        head.update({"Content-Type": "application/json"})
        kwargs['headers'] = head
        return Session.put(self, self.deal_url(url), data, **kwargs)
