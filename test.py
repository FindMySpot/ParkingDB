import json
import requests
import pymongo
import datetime
from pymongo import MongoClient
client = MongoClient()
db = client.parkingDatabase
collection = db.testStation1

spotList = collection.find({'occupied':False, 'reserved':False})
def dtToEpoch(dt):
    return ((dt - datetime.datetime(1970,1,1)).total_seconds())
def handleTimeCalc(dt1, dt2):
    temp = (dt1 - datetime.datetime(1970,1,1)).total_seconds() 
    return datetime.datetime.fromtimestamp(temp)

now = datetime.datetime.utcnow()

for spot in spotList:
    for rs in spot["rTimes"]:
        print(handleTimeCalc( now, rs["date"]))

print("Done")



