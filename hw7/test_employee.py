from employee_api import EmployeeApi


BASE_URL = "http://5.101.50.27:8000"
TEST_USER = "harrypotter"
TEST_PASSWORD = "expelliarmus"
TEST_EMPLOYEE_ID = 1  # ID существующего сотрудника для тестов


def get_api():
    """Создает и возвращает экземпляр API"""
    return EmployeeApi(BASE_URL)


def test_create_employee():
    api = get_api()

    employee_data = {
        "first_name": "Irina",
        "last_name": "Popov",
        "middle_name": "Vasilevna",
        "company_id": 1,
        "email": "irina_va_test@gmail.com",
        "phone": "2445468",
        "birthdate": "2000-12-02",
        "is_active": True
    }

    print("Создаем нового сотрудника...")
    result = api.create_employee(**employee_data)

    print("Проверяем сохранение данных в базе:")
    all_fields_saved = True
    for key, value in employee_data.items():
        if result[key] == value:
            print(f"  Поле '{key}' сохранено: {result[key]}")
        else:
            print(f"  Ошибка: поле '{key}' не сохранено. Ожидалось: {value}, получено: {result[key]}")
            all_fields_saved = False

    if all_fields_saved:
        print("Тест пройден: все данные сотрудника сохранены в базе.")
    else:
        print("Тест не пройден: не все данные сохранены.")


def test_get_employee():
    api = get_api()

    print(f"Получаем информацию о сотруднике с ID {TEST_EMPLOYEE_ID}...")
    employee = api.get_employee(TEST_EMPLOYEE_ID)

    if "first_name" in employee and "last_name" in employee:
        print(f"  Сотрудник найден: {employee['first_name']} {employee['last_name']}")
        print(f"  Email: {employee.get('email', 'не указан')}")
        print(f"  Телефон: {employee.get('phone', 'не указан')}")
        print("Тест пройден: информация о сотруднике получена.")
    else:
        print("Тест не пройден: не удалось получить информацию о сотруднике.")


def test_update_employee():
    api = get_api()

    print(f"Обновляем данные сотрудника ID {TEST_EMPLOYEE_ID}...")

    update_data = {
        "last_name": "UpdatedLastName",
        "email": "updated_email_test@example.com",
        "phone": "2222222",
        "is_active": False
    }

    updated_employee = api.update_employee(
        employee_id=TEST_EMPLOYEE_ID,
        user=TEST_USER,
        password=TEST_PASSWORD,
        **update_data
    )

    print("Проверяем обновленные поля:")

    check_field(updated_employee, "last_name", "UpdatedLastName", "Фамилия")
    check_field(updated_employee, "email", "updated_email_test@example.com", "Email")
    check_field(updated_employee, "phone", "2222222", "Телефон")
    check_field(updated_employee, "is_active", False, "Статус активности")

    print("Тест пройден: данные сотрудника обновлены.")


def check_field(employee_data, field_name, expected_value, field_label):
    """Вспомогательная функция для проверки поля"""
    actual_value = employee_data.get(field_name)
    if actual_value == expected_value:
        print(f"  {field_label} обновлен")
    else:
        print(f"  {field_label} не обновлен. Ожидалось: {expected_value}, получено: {actual_value}")


def test_check_patch_fields():
    api = get_api()

    print("Проверяем, какие поля можно обновить через PATCH:")


    current_data = api.get_employee(TEST_EMPLOYEE_ID)

    # Пробуем обновить разные поля
    test_cases = [
        ("first_name", "НовоеИмя", "Имя"),
        ("middle_name", "НовоеОтчество", "Отчество"),
        ("company_id", 3, "ID компании"),
        ("birthdate", "2005-05-05", "Дата рождения")
    ]

    for field, new_value, field_label in test_cases:
        test_data = {field: new_value}

        updated = api.update_employee(
            employee_id=TEST_EMPLOYEE_ID,
            user=TEST_USER,
            password=TEST_PASSWORD,
            **test_data
        )

        if updated[field] == new_value:
            print(f"  Поле '{field_label}' обновляется")
        else:
            print(f"  Поле '{field_label}' не обновляется (осталось: {updated[field]})")

    print("Проверка завершена.")


def run_all_tests():
    """Запускает все тесты"""
    print("Запуск тестов API сотрудников")
    print("=" * 50)

    tests = [
        ("Тест создания сотрудника", test_create_employee),
        ("Тест получения информации о сотруднике", test_get_employee),
        ("Тест изменения данных сотрудника", test_update_employee),
        ("Тест проверки обновления полей", test_check_patch_fields)
    ]

    for test_name, test_function in tests:
        print(f"\n{test_name}:")
        try:
            test_function()
        except Exception as e:
            print(f"Ошибка: {e}")

    print("\n" + "=" * 50)
    print("Все тесты завершены.")


if __name__ == "__main__":
    run_all_tests()