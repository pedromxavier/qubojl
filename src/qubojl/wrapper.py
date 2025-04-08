import juliacall

class Wrapper(object):
    """
    """

    __ref__ = None

    def __new__(cls):
        if cls.__ref__ is None:
            cls.__ref__ = object.__new__(cls)
            cls.__ref__.__init__()
        
        return cls.__ref__
    
    def __init__(self):
        self.module = juliacall.newmodule("JL")
        self.module.seval("import QUBO")

QUBO = Wrapper().module.QUBO
