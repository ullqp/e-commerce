from typing import Any


class Product:
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

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        """Метод, который инициализирует экземпляры класса."""
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result
