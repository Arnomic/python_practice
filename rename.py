#! /usr/bin/python
import os
import re

'''
重命名视频文件
'''


class Rename:

    def __init__(self):
        pass

    def get_file_list(self):

        file_list = self.get_config()
        print(file_list)
        path = '/Users/dingzhu/Downloads/尚学堂高淇java300集第一季'
        for item in os.listdir(path):
            title = re.match('^([0-9]{2,3})_.*(\.[a-z0-9]{2,4})$', item)
            if title:
                groups = title.groups()
                old_name = path + '/' + title.group(0)
                if file_list.get(groups[0]) and os.path.exists(old_name):
                    new_name = path + '/' + file_list[groups[0]].replace('\n','') + groups[1]
                    print(new_name)
                    # os.rename(old_name, new_name)

    def get_config(self):
        file = open('file_list.txt')
        dicts = {}
        while True:
            item = file.readline()
            if not item:
                break
            value = item.replace("\n", '').split('_')
            dicts[value[0]] = item

        return dicts


# handle = Rename()

# handle.readConfig()
# handle.get_file_list()
