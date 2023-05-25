"""Создание, изменение и удаление нового запроса"""

import pytest
from requests import Response
from utils.api import reqres_api
from utils.checking import Checking



class Test_create_request():

    def test_create_new_request(self, set_up, some, users, pages):

        print("\n" + "Метод POST 1") # для наблюдения, что выполняется
        result_post: Response = reqres_api.create_new_request()
        check_post = result_post.json()
        id = check_post.get("id")
        # проверка статус-кода:
        Checking.check_status_code(result_post, 201)
        #print("Фактический статус код = " + str(result_post.status_code))

        print("\n" + "Метод GET POST 1") # проверяем метод POST 1
        result_get: Response = reqres_api.get_new_request(id)
        # проверка статус-кода:
        Checking.check_status_code(result_get, 200)
        #print("Фактический статус код = " + str(result_post.status_code))

        print("\n" + "Метод GET SINGLE USER NOT FOUND")
        result_get: Response = reqres_api.get_new_request(id)
        # проверка статус-кода:
        Checking.check_status_code(result_get, 200)
        #print("Фактический статус код = " + str(result_post.status_code))

        print("\n" + "Метод PUT 1")
        result_put: Response = reqres_api.put_new_request(id)  
        # проверка статус-кода:
        Checking.check_status_code(result_put, 200)
        #print("Фактический статус код = " + str(result_post.status_code))

        print("\n" + "Метод GET PUT 1") # проверяем метод PUT 1
        result_get: Response = reqres_api.get_new_request(id)
        # проверка статус-кода:
        Checking.check_status_code(result_get, 200)
        #print("Фактический статус код = " + str(result_post.status_code))

        print("\n" + "Метод DELETE")
        result_delete: Response = reqres_api.delete_new_request(id)
        # проверка статус-кода:
        Checking.check_status_code(result_delete, 204)
        #print("Фактический статус код = " + str(result_post.status_code))

        print("\n" + "Метод GET DELETE") # проверяем метод DELETE
        result_get: Response = reqres_api.get_new_request(id)
        # проверка статус-кода:
        Checking.check_status_code(result_get, 200)
        #print("Фактический статус код = " + str(result_post.status_code))

        print("\n" + "Метод PATCH") # проверяем PATCH
        result_patch: Response = reqres_api.patch_new_request(id)
        # проверка статус-кода:
        Checking.check_status_code(result_patch, 200)
        #print("Фактический статус код = " + str(result_post.status_code))
