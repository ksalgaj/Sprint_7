# Sprint_7

# QA Scooter API Tests

Автоматизированные тесты для API сервиса **Scooter**.  
Проект использует Python, pytest и Allure для отчётов.

## Протестированные эндпоинты

- **Курьер**
  - `POST /courier` — создание курьера
  - `POST /courier/login` — авторизация курьера
  - `DELETE /courier/{id}` — удаление курьера

- **Заказы**
  - `POST /orders` — создание заказа
  - `GET /orders` — список заказов
  - `PUT /orders/accept/{id}` — принятие заказа
  - `GET /orders/track?t={track_id}` — получение заказа по треку

---

## Используемые технологии

- Python 3.x  
- pytest  
- requests  
- Allure framework  

---

## Особенности

- Все тесты независимые  
- Используются фикстуры для подготовки данных  
- Генерация Allure-отчётов для визуализации результатов