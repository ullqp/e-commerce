import pytest

from src.utils import Category, LawnGrass, Product, Smartphone


def test_init_product(product_1: Product) -> None:
    assert product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 5


def test_init_category(category_1: Category) -> None:
    assert category_1.name == "Смартфоны"
    assert (
        category_1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )


def test_product_count(category_1: Category) -> None:
    assert Category.product_count == 0


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

    def test_price(product_1: Product, capsys) -> None:
        product_1.price = -100
        captured = capsys.readouterr()
        assert captured.out == "Цена не должна быть нулевая или отрицательная\n"


def test_str_product(product_1: Product) -> None:
    assert str(product_1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_str_category(category_1: Category) -> None:
    assert str(category_1) == "Смартфоны, количество продуктов: 0 шт."


def test_add_products(product_1: Product, product_2: Product) -> None:
    res = product_1 + product_2
    assert res == 1334000


def test_category_iterator(category_iterator: list) -> None:
    assert category_iterator[0].name == "Samsung Galaxy S23 Ultra"
    assert category_iterator[1].name == "Xiaomi Redmi Note 11"


def test_init_smartphone(smartphone1: Smartphone) -> None:
    assert smartphone1.name == "Iphone 15"
    assert smartphone1.description == "512GB, Gray space"
    assert smartphone1.price == 210000.0
    assert smartphone1.quantity == 8
    assert smartphone1.efficiency == 98.2
    assert smartphone1.model == "15"
    assert smartphone1.memory == 512
    assert smartphone1.color == "Gray space"


def test_init_lawngrass(grass1: LawnGrass) -> None:
    assert grass1.name == "Газонная трава"
    assert grass1.description == "Элитная трава для газона"
    assert grass1.price == 500.0
    assert grass1.quantity == 20
    assert grass1.country == "Россия"
    assert grass1.germination_period == "7 дней"
    assert grass1.color == "Зеленый"


def test_add_not_products(smartphone1: Smartphone, grass1: LawnGrass) -> None:
    with pytest.raises(TypeError):
        smartphone1 + grass1


def test_add_not_product(category_1: Category) -> None:
    with pytest.raises(TypeError):
        category_1.add_product("abc")


def test_zero_exception(capsys) -> None:
    with pytest.raises(ValueError) as e:
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    assert str(e.value) == "Товар с нулевым количеством не может быть добавлен"


def test_middle_price(category_3: Category) -> None:
    assert category_3.middle_price() == 11105


def test_middle_price_exception(category_1: Category) -> None:
    assert category_1.middle_price() == 0
