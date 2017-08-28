#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import os
import binascii
from Crypto.Hash import SHA, HMAC
import datetime
from urllib import urlencode
from collections import OrderedDict
import urllib
import json
import random, string

class askapi:

	SIGN_KEY = '42E02265617E4B6DE18A6E991E4CC'
	USER_AGENT = 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; google_sdk Build/KK)'
	HOST = 'api.ask.fm'
	PORT = '443'
	DEVICE_ID = binascii.hexlify(os.urandom(8))
	ANDROID_VERSION = "android_4.4"
	API_VERSION = "1.7"

	def __init__(self):
		self.rt = 1
		params = (
			("did", self.DEVICE_ID),
			("rt", str(self.rt)),
			("ts", self.timemill())
		)

		DATA_SIGN = ""
		for v in params:
			DATA_SIGN += "%" + str(v[0]) + "%"
			DATA_SIGN += urllib.quote(str(v[1]))

		headers = {
		    'X-Client-Type': str(self.ANDROID_VERSION),
		    'Authorization': 'HMAC '+self.generatorSignature("GET", "/token", DATA_SIGN),
		    'X-Api-Version': str(self.API_VERSION),
		    'User-Agent': str(self.USER_AGENT),
		    'Host': self.HOST+":"+self.PORT
		}

		r = requests.get('https://api.ask.fm/token', headers=headers, params=params)
		self.rt += 1
		
		self.accessToken = r.json()['accessToken']

	def login(self, username, password):

		data = {
			'did': str(self.DEVICE_ID),
			'guid': str(self.DEVICE_ID),
			'pass': str(password),
			'rt': str(self.rt),
			'ts': self.timemill(),
			'uid':str(username)
		}
		data = json.dumps(data, sort_keys=False, separators=(',', ':'))
		params = (
			("json", data),
		)
		DATA_SIGN = ""
		for v in params:
			DATA_SIGN += "%" + str(v[0]) + "%"
			DATA_SIGN += urllib.quote(str(v[1]))

		headers = {
		    'X-Client-Type': str(self.ANDROID_VERSION),
		    'X-Access-Token': str(self.accessToken),
		    'Authorization': 'HMAC '+self.generatorSignature("POST", "/authorize", DATA_SIGN),
		    'X-Api-Version': str(self.API_VERSION),
		    'User-Agent': str(self.USER_AGENT),
		    'Host': self.HOST+":"+self.PORT
		}

		r = requests.post('https://api.ask.fm/authorize', headers=headers, data=params)
		self.rt += 1

		self.accessToken = r.json()['accessToken']
		if r.json()['accessToken']:
			self.user = r.json()['user']
			return r.json()
		else:
			return False

	def like(self, qid, uid):

		data = {
			'qid': str(qid),
			'rt': str(self.rt),
			'ts': self.timemill(),
			'uid':str(uid)
		}
		data = json.dumps(data, sort_keys=False, separators=(',', ':'))
		params = (
			("json", data),
		)
		DATA_SIGN = ""
		for v in params:
			DATA_SIGN += "%" + str(v[0]) + "%"
			DATA_SIGN += urllib.quote(str(v[1]))

		headers = {
		    'X-Client-Type': str(self.ANDROID_VERSION),
		    'X-Access-Token': str(self.accessToken),
		    'Authorization': 'HMAC '+self.generatorSignature("PUT", "/users/answers/likes", DATA_SIGN),
		    'X-Api-Version': str(self.API_VERSION),
		    'User-Agent': str(self.USER_AGENT),
		    'Host': self.HOST+":"+self.PORT
		}

		r = requests.put('https://api.ask.fm/users/answers/likes', headers=headers, data=params)
		self.rt += 1

		if r.json()['status']:
			return True
		else:
			return False

	def register(self, uid, email, password, fullName, genderId, birthDate): # username, email, password, FullName, gender : 1 = Famle, 2 = Male, birthDate = 28.8.2017
		data = {
			  "adid": "9cd533c5-6f92-43fe-b49e-bc4a544dcea8",
			  "did": str(self.DEVICE_ID),
			  "gmt_offset": "0",
			  "guid": str(self.DEVICE_ID),
			  "pass": str(password),
			  "referrer": "null",
			  "rt": str(self.rt),
			  "ts": str(self.timemill()),
			  "uid": str(uid),
			  "user": {
			    "avatarUrl": "null",
			    "birthDate": str(birthDate),
			    "email": str(email),
			    "fullName": str(fullName),
			    "uid": str(uid),
			    "lang": "en",
			    "genderId": genderId
			  }
			}
		data = json.dumps(data, sort_keys=False, separators=(',', ':'))
		params = (
			("json", data),
		)

		DATA_SIGN = ""
		for v in params:
			DATA_SIGN += "%" + str(v[0]) + "%"
			DATA_SIGN += urllib.quote(str(v[1]))

		headers = {
		    'X-Client-Type': str(self.ANDROID_VERSION),
		    'X-Access-Token': str(self.accessToken),
		    'Authorization': 'HMAC '+self.generatorSignature("POST", "/register", DATA_SIGN),
		    'X-Api-Version': str(self.API_VERSION),
		    'User-Agent': str(self.USER_AGENT),
		    'Host': self.HOST+":"+self.PORT
		}

		r = requests.post('https://api.ask.fm/register', headers=headers, data=params)
		self.rt += 1

		self.accessToken = r.json()['at']

	def follow(self, uid):

		data = {
			'rt': str(self.rt),
			'ts': self.timemill(),
			'uid':str(uid)
		}
		data = json.dumps(data, sort_keys=False, separators=(',', ':'))
		params = (
			("json", data),
		)
		DATA_SIGN = ""
		for v in params:
			DATA_SIGN += "%" + str(v[0]) + "%"
			DATA_SIGN += urllib.quote(str(v[1]))

		headers = {
		    'X-Client-Type': str(self.ANDROID_VERSION),
		    'X-Access-Token': str(self.accessToken),
		    'Authorization': 'HMAC '+self.generatorSignature("PUT", "/friends", DATA_SIGN),
		    'X-Api-Version': str(self.API_VERSION),
		    'User-Agent': str(self.USER_AGENT),
		    'Host': self.HOST+":"+self.PORT
		}

		r = requests.put('https://api.ask.fm/friends', headers=headers, data=params)
		self.rt += 1

		if r.json()['status']:
			return True
		else:
			return False

	def askSomeone(self, usernames, qBody, type='anonymous'): # types: anonymous,user
		data = {
			'question': {
				'type': str(type),
				'body': str(qBody)
			},
			'rt': str(self.rt),
			'ts': self.timemill(),
			'users':usernames
		}
		data = json.dumps(data, sort_keys=False, separators=(',', ':'))
		params = (
			("json", data),
		)

		DATA_SIGN = ""
		for v in params:
			DATA_SIGN += "%" + str(v[0]) + "%"
			DATA_SIGN += urllib.quote(str(v[1]))

		headers = {
		    'X-Client-Type': str(self.ANDROID_VERSION),
		    'X-Access-Token': str(self.accessToken),
		    'Authorization': 'HMAC '+self.generatorSignature("POST", "/users/questions", DATA_SIGN),
		    'X-Api-Version': str(self.API_VERSION),
		    'User-Agent': str(self.USER_AGENT),
		    'Host': self.HOST+":"+self.PORT
		}

		r = requests.post('https://api.ask.fm/users/questions', headers=headers, data=params)
		self.rt += 1

		if r.json()['status']:
			return True
		else:
			return False
		
	def getQuestions(self, limit=25, offset=0, skip_shoutouts='false'):
		params = (
			("limit", str(limit)),
			("offset", str(offset)),
			("rt", str(self.rt)),
			("skip_shoutouts", str(skip_shoutouts)),
			("ts", self.timemill())
		)


		DATA_SIGN = ""
		for v in params:
			DATA_SIGN += "%" + str(v[0]) + "%"
			DATA_SIGN += urllib.quote(str(v[1]))

		headers = {
		    'X-Client-Type': str(self.ANDROID_VERSION),
		    'X-Access-Token': str(self.accessToken),
		    'Authorization': 'HMAC '+self.generatorSignature("GET", "/my/questions", DATA_SIGN),
		    'X-Api-Version': str(self.API_VERSION),
		    'User-Agent': str(self.USER_AGENT),
		    'Host': self.HOST+":"+self.PORT
		}

		r = requests.get('https://api.ask.fm/my/questions', headers=headers, params=params)
		return r.json()

	def getNotifications(self, limit=25, offset=0, type='ANSWER,SHOUTOUT_ANSWER'): # types: ANSWER,SHOUTOUT_ANSWER,LIKE,PHOTOPOLL_VOTE,GIFT,MENTION,REGISTRATION,FRIEND_JOIN,FRIEND_ANSWER,FRIEND_AVATAR,FRIEND_BACKGROUND,FRIEND_MOOD,PHOTOPOLL,PHOTOPOLL_MENTION,SELF_BULLYING_NOTICE,SELF_BULLYING_WARNING,SELF_BULLYING_BAN [ can choice multiple  type ]
		params = (
			("limit", str(limit)),
			("offset", str(offset)),
			("rt", str(self.rt)),
			("ts", self.timemill()),
			("type", str(type))
		)


		DATA_SIGN = ""
		for v in params:
			DATA_SIGN += "%" + str(v[0]) + "%"
			DATA_SIGN += urllib.quote(str(v[1]))


		headers = {
		    'X-Client-Type': str(self.ANDROID_VERSION),
		    'X-Access-Token': str(self.accessToken),
		    'Authorization': 'HMAC '+self.generatorSignature("GET", "/notifications", DATA_SIGN),
		    'X-Api-Version': str(self.API_VERSION),
		    'User-Agent': str(self.USER_AGENT),
		    'Host': self.HOST+":"+self.PORT
		}

		r = requests.get('https://api.ask.fm/notifications', headers=headers, params=params)
		return r.json()

	def streamProfile(self, uid, limit=25, offset=0):
		params = (
			("limit", str(limit)),
			("offset", str(offset)),
			("rt", str(self.rt)),
			("ts", self.timemill()),
			("uid", str(uid))
		)


		DATA_SIGN = ""
		for v in params:
			DATA_SIGN += "%" + str(v[0]) + "%"
			DATA_SIGN += urllib.quote(str(v[1]))


		headers = {
		    'X-Client-Type': str(self.ANDROID_VERSION),
		    'X-Access-Token': str(self.accessToken),
		    'Authorization': 'HMAC '+self.generatorSignature("GET", "/users/profile/stream", DATA_SIGN),
		    'X-Api-Version': str(self.API_VERSION),
		    'User-Agent': str(self.USER_AGENT),
		    'Host': self.HOST+":"+self.PORT
		}

		r = requests.get('https://api.ask.fm/users/profile/stream', headers=headers, params=params)
		return r.json()

	def userLikes(self, uid, limit=25, offset=0):
		params = (
			("limit", str(limit)),
			("offset", str(offset)),
			("rt", str(self.rt)),
			("ts", self.timemill()),
			("uid", str(uid))
		)


		DATA_SIGN = ""
		for v in params:
			DATA_SIGN += "%" + str(v[0]) + "%"
			DATA_SIGN += urllib.quote(str(v[1]))


		headers = {
		    'X-Client-Type': str(self.ANDROID_VERSION),
		    'X-Access-Token': str(self.accessToken),
		    'Authorization': 'HMAC '+self.generatorSignature("GET", "/users/likes", DATA_SIGN),
		    'X-Api-Version': str(self.API_VERSION),
		    'User-Agent': str(self.USER_AGENT),
		    'Host': self.HOST+":"+self.PORT
		}

		r = requests.get('https://api.ask.fm/users/likes', headers=headers, params=params)
		return r.json()

	def userGifts(self, uid, limit=25, offset=0):
		params = (
			("limit", str(limit)),
			("offset", str(offset)),
			("rt", str(self.rt)),
			("ts", self.timemill()),
			("uid", str(uid))
		)


		DATA_SIGN = ""
		for v in params:
			DATA_SIGN += "%" + str(v[0]) + "%"
			DATA_SIGN += urllib.quote(str(v[1]))


		headers = {
		    'X-Client-Type': str(self.ANDROID_VERSION),
		    'X-Access-Token': str(self.accessToken),
		    'Authorization': 'HMAC '+self.generatorSignature("GET", "/users/gifts", DATA_SIGN),
		    'X-Api-Version': str(self.API_VERSION),
		    'User-Agent': str(self.USER_AGENT),
		    'Host': self.HOST+":"+self.PORT
		}

		r = requests.get('https://api.ask.fm/users/gifts', headers=headers, params=params)
		return r.json()

	def getFriends(self, limit=25, offset=0):
		params = (
			("fav_first", str('true')),
			("limit", str(limit)),
			("name", str('')),
			("offset", str(offset)),
			("rt", str(self.rt)),
			("ts", self.timemill()),
		)


		DATA_SIGN = ""
		for v in params:
			DATA_SIGN += "%" + str(v[0]) + "%"
			DATA_SIGN += urllib.quote(str(v[1]))


		headers = {
		    'X-Client-Type': str(self.ANDROID_VERSION),
		    'X-Access-Token': str(self.accessToken),
		    'Authorization': 'HMAC '+self.generatorSignature("GET", "/users/search", DATA_SIGN),
		    'X-Api-Version': str(self.API_VERSION),
		    'User-Agent': str(self.USER_AGENT),
		    'Host': self.HOST+":"+self.PORT
		}

		r = requests.get('https://api.ask.fm/users/search', headers=headers, params=params)
		return r.json()

	def accountDetails(self, uid):
		params = (
			("rt", str(self.rt)),
			("ts", self.timemill()),
			("uid", str(uid))
		)


		DATA_SIGN = ""
		for v in params:
			DATA_SIGN += "%" + str(v[0]) + "%"
			DATA_SIGN += urllib.quote(str(v[1]))


		headers = {
		    'X-Client-Type': str(self.ANDROID_VERSION),
		    'X-Access-Token': str(self.accessToken),
		    'Authorization': 'HMAC '+self.generatorSignature("GET", "/users/details", DATA_SIGN),
		    'X-Api-Version': str(self.API_VERSION),
		    'User-Agent': str(self.USER_AGENT),
		    'Host': self.HOST+":"+self.PORT
		}

		r = requests.get('https://api.ask.fm/users/details', headers=headers, params=params)
		return r.json()

	def getWall(self, limit=25, ffrom=0): # ffrom = last answer. 0 = from begin
		params = (
			("from", str(ffrom)),
			("limit", str(limit)),
			("rt", str(self.rt)),
			("ts", self.timemill())
		)


		DATA_SIGN = ""
		for v in params:
			DATA_SIGN += "%" + str(v[0]) + "%"
			DATA_SIGN += urllib.quote(str(v[1]))


		headers = {
		    'X-Client-Type': str(self.ANDROID_VERSION),
		    'X-Access-Token': str(self.accessToken),
		    'Authorization': 'HMAC '+self.generatorSignature("GET", "/wall", DATA_SIGN),
		    'X-Api-Version': str(self.API_VERSION),
		    'User-Agent': str(self.USER_AGENT),
		    'Host': self.HOST+":"+self.PORT
		}

		r = requests.get('https://api.ask.fm/wall', headers=headers, params=params)
		return r.json()

	def setAccessToken(self, accessToken):
		self.accessToken = accessToken

	def getAccessToken(self):	
		return self.accessToken

	def generatorSignature(self, method, endpoint, data):
		return HMAC.new(self.SIGN_KEY, method+"%"+self.HOST+":"+self.PORT+"%"+endpoint+data, SHA).hexdigest() # Pattern METHOD%HOST:PORT%ENDPOINT%DATA

	def timemill(self):
		return str(int((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds() * 1000))


if __name__ == "__main__":
	print "can't run this file."
