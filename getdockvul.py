# -*- coding: utf-8 -*-
import os
import re

import os
def getListFiles(path):
    ret = []
    for root, dirs, files in os.walk(path):
        for filespath in files:
            ret.append(os.path.join(root,filespath))
    return ret
if __name__ == '__main__':
    ret = getListFiles("/root/PycharmProjects/docker/vulhub")
    for each in ret:
        if each.find('README.md') != -1:
            f=open(each,'r')
            for list in f.readlines():
                name = unicode(list, "utf-8")
                if list.find('http://your-ip:') != -1:
                    a = re.search(r'http://your-ip:(\d+)', list).group(1)
                    dirs= each.split('README.md')[0].replace('/root/PycharmProjects/docker/','')
                    print dirs,a

            f.close()
