from __future__ import unicode_literals

from django.db import models

import pymongo

import urllib

from pymongo import MongoClient

from urllib import quote_plus

client = MongoClient('mongodb://localhost:27017/')

# var x = new Mongo('host[:27017]')




db = Client["Fund"]
# collection = db["User"]
user = {
	"first_name" : "Andre",
	"last_name" : "Wilkinson",
	"email" : "andre_w3@yahoo.com",
	"account" : "[10000]"	
}

db = client.Fund
db.user.insert(dre)

for a in db.user.find():
	pprint.pprint(a)
# user ["first_name"] = "andre"
# user ["last_name"] = "wilkinson"
# user ["email"] = "andre_w3@yahoo.com"
# collection.insert(user)


# Create your models here.
