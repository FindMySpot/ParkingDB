import pymongo
from pymongo import MongoClient
import datetime
import time

client = MongoClient("mongodb://db:27017")
#client = MongoClient()
db = client.parkingDatabase
stations = ['testStation1', 'testStation2', 'testStation3', 'testStation4', 'testStation5', 'testStation6', 'testStation7', 'testStation8', 'testStation9', 'testStation10', 'testStation11', 'testStation12', 'testStation13', 'testStation14', 'testStation15']

def dtToEpoch(dt):
    return ((dt - datetime.datetime(1970,1,1)).total_seconds())

def epochToDt(ep):
    return datetime.datetime.fromtimestamp(ep)

def compareDt(ep1, ep2):
    return (((dtToEpoch(ep1) - dtToEpoch(ep2))/60) < 60 and ((dtToEpoch(ep1)-dtToEpoch(ep2))/60)>0)

#after 30 mins, get rid of reserved status
def compareDtGEQ(ep1, ep2): 
    return (((dtToEpoch(ep2) - dtToEpoch(ep1))/60) > 30)

print("Initialized reservation checker")
while True: 
    
    print("CHECK---------------------------------")
    now = datetime.datetime.utcnow()
    for s in stations:
        #print("Loop1")
        for spot in db[s].find():
            #print("Loop2")
            tempId = spot["id"] 
            if spot["rTimes"] != []:
                for rBook in spot["rTimes"]:
                    if(compareDt(rBook["date"], now)):
                        db[s].update({'id':tempId},{'$set':{'reserved':True}})
                        print("Updated a reservation status")
                        print(spot)

    for s in stations:
        for spot in db[s].find():
            tempId = spot["id"]
            if spot["rTimes"] == []:
                db[s].update({'id':tempId}, {'$set':{'reserved':False}})
            else:
                for rBook in spot["rTimes"]:
                    print(dtToEpoch(rBook["date"]))
                    print(dtToEpoch(now))
                    print((dtToEpoch(rBook["date"]) - dtToEpoch(now))/60)
                    if(compareDtGEQ(rBook["date"], now)):
                        #update reserved to false, then get rid of the old reservation
                        db[s].update({'id':tempId}, {'$set':{'reserved':False}})
                        db[s].update({'id':tempId}, {'$pull':{'rTimes':{'date':rBook['date']}}})
                        print("Got rid of old reservation")
    time.sleep(5)
