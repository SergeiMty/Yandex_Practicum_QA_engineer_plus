# Импорт необходимых модулей и данных для запроса
import requests
import configuration
import request_data as data

# Определение функции для отправки POST-запроса на поиск наборов по продуктам
def post_new_user(user_body):
    # Отправка POST-запроса с использованием URL из конфигурации, данных о продуктах и заголовков
    # Возвращается объект ответа, полученный от сервера
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=user_body)  

response = post_new_user(data.user_body)


def post_new_client_kit(kit_body, auth_token):
    headers = data.kits_headers.copy()
    headers["Authorization"] = "Bearer " + auth_token 
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH, json = kit_body, 
                         headers= headers)



