# encoding:utf8
# Name  : main.py
# Author: Aron
# Date  : 2014-08-14
# Desc  : main program for hackathon
#
import time
from webo import WeboClient

# get user's data
def get_weight(follower_cnt, friends_cnt):
    return 0.1 * follower_cnt + 0.9 * friends_cnt

def get_friends_list():
    webo = WeboClient("conf.in")
    webo.run()
    friends_dict = {}
    friends_timeline = webo.get_friends_timeline()
    id_to_name = {}
    ids = {}
    id_c = 0
    fris = []
    for _fri in friends_timeline:
        friends_dict = {}
        friends_dict["name"]    = _fri["user"]["screen_name"]  # 微博名字
        friends_dict["text"]    = _fri["text"]                 # 微博内容
        friends_dict["img"]     = _fri["user"]["avatar_hd"]    # 微博avatar
        friends_dict["weight"]  = get_weight(_fri["user"]["followers_count"],\
                                             _fri["user"]["friends_count"])

        friends_dict["follow_me"] = _fri["user"]["follow_me"]
        friends_dict["following"] = _fri["user"]["following"]
        fris.append(friends_dict)
        id_to_name[id_c] = friends_dict["name"]
        ids[friends_dict["name"]]= _fri["user"]["id"]
        id_c += 1
    relations = []
    """
    for i in range(len(id_to_name.keys())):
        for j in range(i,len(id_to_name.keys())):
            if i != j:
                rela = webo.get_relation(ids[id_to_name[i]], ids[id_to_name[j]])
                if rela:
                    relations.append((i,j))
                time.sleep(0.3)
    """
    files = open("friends_list", "w")
    for _fri in fris:
        print _fri["name"], type(_fri["name"])
        
        files.write(_fri["name"].encode('utf-8') + "\t")
        files.write(_fri["text"].encode('utf-8') + "\t")
        files.write(_fri["img"].encode('utf-8') + "\t")
        files.write(str(_fri["weight"]) + "\t")
        files.write(str(int(_fri["follow_me"])) + "\t")
        files.write(str(int(_fri["following"])) + "\n")
    """
    for _r in relations:
        files.write(str(r[0]) + "\t" + str(r[1]))
    """
    files.close()

if __name__ == '__main__':
    get_friends_list()
    import os
    os.system("OpenGL.exe")
    
    
