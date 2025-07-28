import sender_stand_request
import request_data as data
    
# Функция для изменения значения в параметре Name в теле запроса 
def get_kit_body(name):
    current_kits_body = data.kits_body.copy()
    current_kits_body["name"] = name
    return current_kits_body
# Функция получения токена
def get_new_user_token():
    user_body= data.user_body.copy()
    response_user = sender_stand_request.post_new_user(user_body)
    return response_user.json()["authToken"]
print(get_new_user_token())

# Функция для позитивной проверки
def positive_assert(kit_body):
    kit_response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert kit_response.status_code==201
    assert kit_response.json()["name"]== kit_body["name"]

# Функция для негативной проверки

def negative_assert_symbol(kit_body):
    kit_response = sender_stand_request.post_new_client_kit(kit_body,get_new_user_token())
    assert kit_response.status_code==400

    
# Тест 1. Успешное создание пользователя. Параметр name состоит из 1 символа
def test_create_kit_1_letter_in_first_name_get_success_response():
    positive_assert(get_kit_body("a"))
    
# Тест 2. Успешное создание пользователя. Параметр name состоит из 511 символов
def test_create_kit_511_letter_in_first_name_get_success_response():
    positive_assert(
        get_kit_body(
            "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
            "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
            "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
            "dabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
            "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
            "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
            "cdabcdabcdabcdabcdabcdabcdabcdabC"
        )      
    )  
    
# Тест 3. Ошибка. Параметр name состоит из 0 символов
def test_create_kit_0_letter_in_first_name_get_error_response():
    negative_assert_symbol(get_kit_body(""))
    
# Тест 4. Ошибка. Параметр name состоит из 512 символов
def test_create_kit_512_letter_in_first_name_get_error_response():
    negative_assert_symbol(
        get_kit_body(
        "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
            "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
            "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
            "dabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
            "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
            "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
            "cdabcdabcdabcdabcdabcdabcdabcdabCd"    
        )      
    )  
    
# Тест 5. Успешное создание пользователя. Параметр Name состоит из английских букв
def test_create_kit_english_letter_in_first_name_get_success_response():
    positive_assert(get_kit_body("QWErty"))
    
# Тест 6. Успешное создание пользователя. Параметр name состоит из русских букв
def test_create_kit_russian_letter_in_first_name_get_success_response():
    positive_assert(get_kit_body("Мария"))
    
# Тест 7. Успешное создание пользователя. Параметр name состоит из из строки спецсимволов 
def test_create_kit_has_space_in_first_name_get_error_response():
    positive_assert(get_kit_body("№%@"))
    
# Тест 8. Успешное создание пользователя. Параметр name состоит из слов с пробелами
def test_create_kit_has_special_symbol_in_first_name_get_error_response():
    positive_assert(get_kit_body ("Человек и КО"))
    
# Тест 9. Успешное создание пользователя. Параметр name состоит из строки цифр
def test_create_kit_has_number_in_first_name_get_error_response():
    positive_assert(get_kit_body("123"))
    
# Тест 10.Ошибка. Параметр не передан в запросе
def test_create_kit_without_name_and_get_error_response():
    kit_body = data.kits_body.copy()
    kit_body.pop("name")
    negative_assert_symbol(kit_body)

# Тест 11.Ошибка. Передан другой тип параметра
def test_create_kit_with_number_type_in_name_get_error_response():
    kit_body = get_kit_body(123)
    negative_assert_symbol(kit_body)

    

    