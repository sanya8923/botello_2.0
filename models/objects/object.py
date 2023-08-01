from typing import Optional
from abc import ABC, abstractmethod


class Object(ABC):
    def __init__(self):
        self.id: Optional[int] = None
