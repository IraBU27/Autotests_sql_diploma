# Ирина Бурцева, 8а группа — Финальный проект. Инженер по тестированию плюс
import configuration
import requests
import data

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER, json=body)
response = post_new_order(data.order_body)
print(response.json()["track"])

def positive_assert(test_numb):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER +"?t=" + str(test_numb))
    assert ord_response.status_code == 200

def test_get_order_right_number_get_success_response():
    positive_assert(response.json()["track"])