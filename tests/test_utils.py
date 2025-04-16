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
        [],
    )


def test_init_category(category_1: Category) -> None:
    assert category_1.name == "Смартфоны"
    assert (
        category_1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )


def test_product_count(category_1: Category) -> None:
    assert Category.product_count == 0


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


def test_add_product(product_1: Product, category_1: Category) -> None:

    category_1.add_product(product_1)
    assert category_1.product_count == 1
    assert "Samsung Galaxy S23 Ultra" in category_1.products


def test_new_product(product_1: Product) -> None:
    new_product = Product.new_product(
        {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8}
    )
    assert new_product.name == "Iphone 15"
    assert new_product.description == "512GB, Gray space"
    assert new_product.price == 210000.0
    assert new_product.quantity == 8

    def test_price(product_1, capsys) -> None:
        product_1.price = -100
        captured = capsys.readouterr()
        assert captured.out == "Цена не должна быть нулевая или отрицательная\n"
