__all__ = ["Singleton"]


class Singleton(type):
    """
    Singleton to avoid multiple instances of a class
    """

    _instances: object = {}

    @classmethod
    def __call__(cls, *args, **kwargs) -> None:
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls
            ).__call__(*args, **kwargs)
        return cls._instances[cls]
