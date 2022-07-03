from yaml import load
try:
    from yaml import CSafeLoader as SafeLoader
except Exception:
    from yaml import SafeLoader


class Config:
    ote = False
    secret = None
    key = None
    domain = None
    name = None
    ttl = 600

    def __init__(self, fn: str):
        with open(fn, 'r', encoding='UTF-8') as f:
            t = load(f.read(), SafeLoader)
        if t is None:
            raise ValueError('Can not load config file.')
        if 'ote' in t:
            v = t['ote']
            if isinstance(v, bool):
                self.ote = v
            del v
        if 'secret' not in t:
            raise ValueError('secret is needed.')
        v = t['secret']
        if not isinstance(v, str):
            raise ValueError('secret must be str.')
        self.secret = v
        if 'key' not in t:
            raise ValueError('key is needed.')
        v = t['key']
        if not isinstance(v, str):
            raise ValueError('key must be str.')
        self.key = v
        if 'domain' not in t:
            raise ValueError('domain is needed.')
        v = t['domain']
        if not isinstance(v, str):
            raise ValueError('domain must be str.')
        self.domain = v
        if 'name' not in t:
            raise ValueError('name is needed.')
        v = t['name']
        if not isinstance(v, str):
            raise ValueError('name must be str.')
        self.name = v
        if 'ttl' in t:
            v = t['ttl']
            if isinstance(v, int) and v < 600:
                raise('ttl must be a integer and must >= 600.')
