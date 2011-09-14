class Stub(dict):
    def __init__(self, **kwargs):
        super(Stub, self).__init__(kwargs)
        for attr in kwargs:
            setattr(self, attr, kwargs[attr])
        dict.__init__(self)

    def make_chain(self):
        return Stub.StubMaker(self)

    class StubMaker(object):
        def __init__(self, parent_stub):
            self.parent_stub = parent_stub

        def __getattr__(self, key):
            if hasattr(self.parent_stub, key):
                value = getattr(self.parent_stub, key)
                return StubMaker(value) if value is Stub else value
            else:
                value = Stub()
                setattr(self.parent_stub, key, value)
                return Stub.StubMaker(value)

        def __setattr__(self, key, value):
            if key == "parent_stub":
                return object.__setattr__(self, key, value)
            setattr(self.parent_stub, key, value)
            return value


