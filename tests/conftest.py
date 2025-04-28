from typing import Generator

import pytest

from src.utils import Category, CategoryIterator, Product


@pytest.fixture(autouse=True)
def reset_counters() -> Generator:
    """Сбрасывает счетчики перед каждым тестом"""
    Category.category_count = 0
    Category.product_count = 0
    yield


@pytest.fixture
def product_1() -> Product:
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def product_2() -> Product:
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture()
def category_1() -> Category:
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [],
    )


@pytest.fixture()
def category_3(product_1: Product, product_2: Product) -> Category:
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product_1, product_2],
    )


@pytest.fixture()
def categories() -> tuple[Category, Category]:
    category_1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        ["Samsung", "Iphone", "Xiaomi"],
    )

    category_2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        ["Телевизор", "Телефон", "Планшет"],
    )
    return category_1, category_2


@pytest.fixture
def category_iterator(category_3: Category) -> list:
    category_iterator = CategoryIterator(category_3)
    return list(category_iterator)
