

def do_normalize(normalize, name):
    return name.replace(" ", "_") if normalize else name


class EasyDict(dict):
    def __init__(self, mapping=None, *, normalize=False, **kwargs):
        if mapping is None:
            kwargs = {
                do_normalize(normalize, k): v for k, v in kwargs.items()
            }
            super().__init__(**kwargs)
        else:
            mapping = {
                do_normalize(normalize, k): v for k, v in mapping.items()
            }
            super().__init__(mapping)

        super().__setitem__("normalize", normalize)

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError as ke:
            raise AttributeError from ke

    def __setattr__(self, name, value):
        self[name] = value

    def __getitem__(self, name):
        return super().__getitem__(self.do_normalize(name))
    
    def __setitem__(self, name, value):        
        return super().__setitem__(self.do_normalize(name), value)

    def get(self, name, default=None):
        return super().get(self.do_normalize(name), default)
        
    def do_normalize(self, name):
        return do_normalize(super().__getitem__("normalize"), name)
