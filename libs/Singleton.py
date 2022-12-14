class Singleton(type):

    def __init__(cls, name, bases, **kwargs):
        super(Singleton, cls).__init__(name, bases, **kwargs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance
