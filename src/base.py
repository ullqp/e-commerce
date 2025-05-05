from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other) -> int:
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        pass

    @price.setter
    @abstractmethod
    def price(self, *args) -> None:
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, **kwargs) -> Any:
        pass

    @classmethod
    @abstractmethod
    def get_all_products(cls) -> list:
        pass


class PrintMixin:

    def __init__(self):
        print(f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity}))")
