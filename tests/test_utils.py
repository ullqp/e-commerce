from typing import Generator

import pytest

from src.utils import Category, Product


@pytest.fixture(autouse=True)
def reset_counters() -> Generator:
    """Сбрасывает счетчики перед каждым тестом"""
    Category.category_count = 0
    Category.product_count = 0
    yield


@pytest.fixture
def product_1() -> Product:
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


def test_init_product(product_1: Product) -> None:
    assert product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 5


@pytest.fixture()
def category_1() -> Category:
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        ["Samsung", "Iphone", "Xiaomi"],
    )


def test_init_category(category_1: Category) -> None:
    assert category_1.name == "Смартфоны"
    assert (
        category_1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category_1.products == ["Samsung", "Iphone", "Xiaomi"]


def test_product_count(category_1: Category) -> None:
    assert Category.product_count == 3


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


def test_categories(categories: Category) -> None:
    assert Category.category_count == 2
