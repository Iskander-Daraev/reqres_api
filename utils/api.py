"""Методы для тестирования reqres api"""

from unittest import result
from utils.http_methods import Http_methods
from pytest import ExitCode
import json
from requests import Response

base_url = "https://reqres.in" # Базовая URL

class reqres_api():


    """Метод  POST"""

    @staticmethod
    def create_new_request():
        json_for_create_new_request = {
            "name": "morpheus",
            "job": "leader"
        }
        post_resource = "/api/users"  # Ресурс метода Post
        post_url = base_url + post_resource
        print(post_url)  # выводим на печать url, чтобы видеть, куда именно мы направляем наш запрос
        result_post = Http_methods.post(post_url, json_for_create_new_request)
        print(result_post.text)  # выводим на печать результат нашего запроса
        return result_post

    """Метод GET"""

    @staticmethod
    def get_new_request(id):

        get_resource = "/api/users?page=2"

        get_url = base_url + get_resource + "&id" + id
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get

    """Метод PUT"""

    @staticmethod
    def put_new_request(id):

        put_resource = "/api/users/2"  # Ресурс метода put

        put_url = base_url + put_resource
        print(put_url)
        json_for_update_new_request = {
            "id": id,
            "name": "morpheus",
            "job": "zion resident"
        }
        result_put = Http_methods.put(put_url, json_for_update_new_request)
        print(result_put.text)
        return result_put

    """Метод DELETE"""

    @staticmethod
    def delete_new_request(id):

        delete_resource = "/api/users/2"

        put_url = base_url + delete_resource
        print(put_url)
        json_for_delete_new_request = {}
        result_delete = Http_methods.delete(put_url, json_for_delete_new_request)
        print(result_delete.text)
        return result_delete


    """Метод PATCH"""

    @staticmethod
    def patch_new_request(id):

        patch_resource = "/api/users/2"
        patch_url = base_url + patch_resource
        print(patch_url)
        json_for_patch_new_request = {
            "name": "morpheus",
            "job": "zion resident"
        }
        result_patch = Http_methods.put(patch_url, json_for_patch_new_request)
        print(result_patch.text)
        return result_patch


"""

        ####################GET SINGLE USER :

        @staticmethod
        def get_new_request(id):

            get_resource = "/api/users/2"
            get_url = base_url + get_resource
            print(get_url)
            result_get = Http_methods.get(get_url)
            print(result_get.text)
            return result_get


        ####################GET SINGLE USER not found:

        @staticmethod
        def get_new_request(id):

            get_resource = "/api/users/23"
            get_url = base_url + get_resource
            print(get_url)
            result_get = Http_methods.get(get_url)
            print(result_get.text)
            return result_get

            ####################GET LIST RESOURCE :

            get_resource = "/api/unknown"

            get_url = base_url + get_resource
            print(get_url)
            result_get = Http_methods.get(get_url)
            print(result_get.text)
            return result_get

            ####################GET SINGLE <RESOURCE>

            get_resource = "/api/unknown/2"

            get_url = base_url + get_resource
            print(get_url)
            result_get = Http_methods.get(get_url)
            print(result_get.text)
            return result_get

            ####################GET  SINGLE <RESOURCE> NOT FOUND

            get_resource = "/api/unknown/23"
            get_url = base_url + get_resource
            print(get_url)
            result_get = Http_methods.get(get_url)
            print(result_get.text)
            return result_get

        ####################POST REGISTER SUCCESFUL

        @staticmethod
        def create_new_request():

            json_for_create_new_request = {
                "email": "eve.holt@reqres.in",
                "password": "pistol"
            }
            post_resource = "/api/register"
            post_url = base_url + post_resource
            print(post_url)
            result_post = Http_methods.post(post_url, json_for_create_new_request)
            print(result_post.text)
            return result_post

        ####################POST REGISTER UNSUCCESFUL

        @staticmethod
        def create_new_request():

            json_for_create_new_request = {
                "email": "sydney@fife"
            }
            post_resource = "/api/register"
            post_url = base_url + post_resource
            print(post_url)
            result_post = Http_methods.post(post_url, json_for_create_new_request)
            print(result_post.text)
            return result_post

        ####################POST LOGIN SUCCESFUL

        @staticmethod
        def create_new_request():

            json_for_create_new_request = {
                "email": "eve.holt@reqres.in",
                "password": "cityslicka"
            }
            post_resource = "/api/login"
            post_url = base_url + post_resource
            print(post_url)
            result_post = Http_methods.post(post_url, json_for_create_new_request)
            print(result_post.text)
            return result_post

        ####################POST LOGIN UNSUCCESFUL

        @staticmethod
        def create_new_request():

            json_for_create_new_request = {
                "email": "peter@klaven"
            }
            post_resource = "/api/login"
            post_url = base_url + post_resource
            print(post_url)
            result_post = Http_methods.post(post_url, json_for_create_new_request)
            print(result_post.text)
            return result_post

        ####################GET DELAYED RESPONSE
        @staticmethod
        def get_new_request(id):

            get_resource = "/api/users?delay=3"
            get_url = base_url + get_resource
            print(get_url)
            result_get = Http_methods.get(get_url)
            print(result_get.text)
            return result_get

"""
