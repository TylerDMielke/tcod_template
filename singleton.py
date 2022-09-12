import logging as log
from typing import Any


def singleton(cls, *args, **kwargs) -> Any:
    instances = {}
    def _singleton(*args, **kwargs) -> Any:
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        else:
            log.debug(f'Tried instantiating more than one instance of {cls} but {cls} is a singleton!')
        return instances[cls]
    return _singleton
