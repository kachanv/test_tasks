# -*- coding: utf-8 -*-
import requests


class Reqres():

    def __init__(self, url="https://reqres.in/", url_users="api/users/"):
        self.url = url
        self.url_users = url_users

    @staticmethod
    def __get_content(content_url):
        content = requests.get(url=content_url)
        content.raise_for_status()
        return content.json()

    def get_users(self):
        return self.__get_content(content_url=self.url + self.url_users)

    def get_user(self, id_user):
        return self.__get_content(content_url=self.url + self.url_users + str(id_user))
