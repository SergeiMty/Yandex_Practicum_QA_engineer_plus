# Импорт необходимых модулей и данных для запроса
import requests
import configuration          # URL_SERVICE, CREATE_ORDER, GET_TRACK
import request_data as data   # headers

#Создание заказа
def post_new_order(body):
    url = configuration.URL_SERVICE + configuration.CREATE_ORDER
    return requests.post(url, json=body, timeout=10)

# Получить заказ по треку ?t=...
def get_track_order(track):
    url = configuration.URL_SERVICE + configuration.GET_TRACK
    return requests.get(url, params={"t": str(track)}, timeout=10)



