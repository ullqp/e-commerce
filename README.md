# Учебный проект "E-commerce"

## Описание:

Проект "E-commerce" - это ядро для интернет-магазина.


## Установка:

Клонируйте репозиторий:
```
git clone https://github.com/ullqp/e-commerce.git
```


## Использование:

Основные классы:

**Product** - товар магазина

**Category** - категория товаров

```python
# Пример использования класса Product
from src.utils import Product

# Создание товара
iphone = Product(
    name="iPhone 15 Pro",
    description="Флагманский смартфон Apple",
    price=1299.99,
    quantity=10
)

print(iphone.price) 

# Пример использования класса Category
from src.utils import Category

# Создание категории с товарами
phones = [
    Product("Galaxy S23", "Флагман Samsung", 999.99, 5),
    Product("Pixel 7", "Смартфон от Google", 699.99, 8)
]

smartphones = Category(
    name="Смартфоны",
    description="Мобильные устройства",
    products=phones
)

print(len(smartphones.products))  
```


### Тестирование

Для тестирования проекта используется библиотека `pytest`. Чтобы запустить тесты, выполните команду:

```bash
pytest
```
Тесты покрывают следующие модули и функции:
- `utils`: классы `Product` и `Category`.

Покрытие тестами составляет более 80% кода проекта.

---