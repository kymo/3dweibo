# encoding:utf8
# Name   : webo.py
# Author : Aron
# Time   : 2014-08-16
# Desc   : Webo description
#
import urllib2
try:
    import json
except:
    import simplejson as json
import httplib

AUTH_URL = "https://api.weibo.com/oauth2/authorize"
ACCESS_URL = "api.weibo.com"
API_URI = "https://api.weibo.com/"


class WeboClient:
    """ we bo client authentication """
    def __init__(self, conf):
        conf_file = open(conf, "r")
        dit = {}
        for line in conf_file.readlines():
            data = line.strip().split(' ')
            dit[data[0]] = data[1]
        self.app_key = dit["app_key"]
        self.app_secret = dit["app_secret"]
        self.redirect_uri = dit["redirect_uri"]
        self.access_token = ""
        self.expire_in = 0
        self.code = ""
    
    def get_authenticate_url(self):
        url = "%s?client_id=%s&response_type=code&redirect_uri=%s"
        return url % (AUTH_URL, self.app_key, self.redirect_uri)

    def get_access_token(self):
        print 'visit the followting url:'
        print self.get_authenticate_url()
        print 'input the code in the redirect url.'
        self.code = raw_input()
        host = ACCESS_URL
        url = "/oauth2/access_token?client_id=%s&client_secret=%s&grant_type=authorization_code&redirect_uri=%s&code=%s"
        url = url % (self.app_key, self.app_secret, self.redirect_uri, self.code)
        conn = httplib.HTTPSConnection(host, 443)
        conn.request(method = "POST", url = url)
        res = conn.getresponse()
        obj = json.loads(res.read())
        self.access_token = obj["access_token"]
        self.expire_in = obj["expires_in"]

    def get_friends_timeline(self):
        #acc = raw_input()
        #self.access_token = acc
        url = "%s2/statuses/friends_timeline.json?access_token=%s&count=50" % (API_URI, self.access_token)
        print url
        req = urllib2.urlopen(url)
        obj = json.loads(req.read())
        return obj["statuses"]
    
    def get_followers(self, screen_name):
        url = "%s2/friendships/friends.json?access_token=%s&screen_name=%s" % (API_URI, self.access_token, screen_name)
        req = urllib2.urlopen(url)
        obj = json.loads(req.read())
        screens = []
        for i in obj["users"]:
            screens.append(i["screen_name"])
        return screens

    def get_relation(self, source_screen, target_screen):
        url = "%s2/friendships/show.json?access_token=%s&source_id=%s&target_id=%s" % \
              (API_URI, self.access_token, source_screen, target_screen)
        req = urllib2.urlopen(url)
        obj = json.loads(req.read())
        if obj['target']['following'] == True or obj['target']['followed_by'] == True:
            return True
        else:
            return False
        
    def run(self):
        self.get_access_token()
        

