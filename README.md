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

**Smartphone** - категория смартфонов

**LawnGrass** - категория газонной травы

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

# Пример использования класса Smartphone
from src.utils import Smartphone

# Создание смартфона
iphone15 = Smartphone(
    name="iPhone 15 Pro",
    description="Флагманский смартфон Apple",
    price=1299.99,
    quantity=10, 
    efficiency= 98.2, 
    model = "15",
    memory = 512, 
    color = "Gray space"
)

print(iphone15.model) 

# Пример использования класса LawnGrass
from src.utils import LawnGrass

# Создание газонной травы
grass = LawnGrass(
    "Газонная трава", 
    "Элитная трава для газона", 
    500.0, 
    20, 
    "Россия", 
    "7 дней", 
    "Зеленый")

print(grass.color) 
```


### Тестирование

Для тестирования проекта используется библиотека `pytest`. Чтобы запустить тесты, выполните команду:

```bash
pytest
```
Тесты покрывают следующие модули и функции:
- `utils`: классы `Product` и `Category`, `Smartphone` и `LawnGrass`'.

Покрытие тестами составляет более 80% кода проекта.

---