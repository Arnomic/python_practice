# !/usr/bin/python

import math


class Vehicle:
    def __init__(self):
        pass

    def run(self):
        pass

    def practice1(self):
        '''
        数据类型
        int
        float
        string
        boolean

        list
        tuple

        set
        dict
        '''
        a = [1]
        t = (a, 23)
        a.append(2)
        print('{},{}'.format(id(a), id(t[0])))
        a = []
        t[0].append(3)
        print('{},{}'.format(id(a), id(t[0])))

        print(max(set(['w', 's', 'z'])))

        x, y, z = {'a': 1, 'b': 2, 'c': 3}
        print(x, y, z)

        print(isinstance(1, (bool, str)))

        try:
            ss = 0 / 0
        except ZeroDivisionError:
            pass

        def by_name(t):
            print(t)
            return 0

        ls = [{}, 2, 3, 4]
        sorted(ls, key=by_name)

    def practice2(self):

        return None


handle = Vehicle()
# handle.run()

# inputThings = input('please type some words: ')

# handle.practice2()


def log(func):
    print('sssss')
    return func


@log
def nice():
    print('xxx')
    return 1


nice()