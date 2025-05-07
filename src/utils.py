from typing import Any

from src.base import BaseProduct, PrintMixin


class Product(BaseProduct, PrintMixin):
    """Класс для представления продуктов."""

    name: str
    description: str
    price: float
    quantity: int

    all_products: list = []

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Метод, который инициализирует экземпляры класса."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        Product.all_products.append(self)
        super().__init__()

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other) -> int:
        if type(self) == type(other):
            return int(self.price * self.quantity + other.price * other.quantity)
        raise TypeError

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if self.__price > new_price:
                user_answer = input("Вы точно хотите поменять цену?\n")
                if user_answer.lower() == "y":
                    self.__price = new_price
                else:
                    print("Действие отменено.")

    @classmethod
    def new_product(cls, product_data: dict) -> Any:
        name = product_data["name"]
        description = product_data["description"]
        price = product_data["price"]
        quantity = product_data["quantity"]

        for product in Product.get_all_products():
            if name == product.name:
                product.quantity += quantity
                product.__price = max(product.__price, price)
                return product

        return cls(name=name, description=description, price=price, quantity=quantity)

    @classmethod
    def get_all_products(cls) -> list:
        return cls.all_products


class Category:
    """Класс для представления категорий."""

    name: str
    description: str
    __products: list

    all_products_count = 0  # Общее количество товаров в категории (по всем продуктам)
    category_count = 0  # Счетчик категорий
    product_count = 0  # Счетчик продуктов

    def __init__(self, name: str, description: str, products: list):
        """Метод, который инициализирует экземпляры класса."""
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def calculate_total_products(self) -> None:
        """Пересчитывает общее количество товаров в категории (сумма quantity всех продуктов)."""
        self.all_products_count = 0
        for product in self.__products:
            self.all_products_count += product.quantity

    def __str__(self) -> str:
        """Возвращает строковое представление категории с количеством товаров."""
        self.calculate_total_products()
        return f"{self.name}, количество продуктов: {self.all_products_count} шт."

    def add_product(self, product: Any) -> None:
        """Добавляет продукт в категорию."""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self) -> str:
        """Возвращает строку с информацией о всех продуктах в категории."""
        result = ""
        for product in self.__products:
            result += str(product)
            result += "\n"
        return result

    @property
    def products_list(self) -> list["Product"]:
        """Возвращает список продуктов в категории."""
        return self.__products


class CategoryIterator:
    """Итератор для переборов товаров одной категории."""

    category: Category
    all_products: list
    current_index: int

    def __init__(self, category: Category) -> None:
        self.category = category
        self.category_products = category.products_list

    def __iter__(self):
        self.current_index = -1
        return self

    def __next__(self) -> Product | None:
        if self.current_index + 1 < len(self.category_products):
            self.current_index += 1
            return self.category_products[self.current_index]
        raise StopIteration


class Smartphone(Product):
    """Класс для представления смартфонов."""

    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        """Метод, который инициализирует экземпляры класса."""

        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс для представления газонной травы."""

    country: str
    germination_period: str
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        """Метод, который инициализирует экземпляры класса."""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
