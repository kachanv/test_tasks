# -*- coding: utf-8 -*-

from external_module import Reqres

if __name__ == '__main__':
    reqres = Reqres()
    print('Users data:\n', reqres.get_users())

    print('\nUser data:')
    for id_user in range(1, 10):
        print(reqres.get_user(id_user=id_user))
