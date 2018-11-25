import threading
import pymongo
import datetime
import time
import pprint
import requests
import json

from pymongo import MongoClient
class sensorThread (threading.Thread):
    def __init__(self, url_, header_, db_, collection_, keys_):
        threading.Thread.__init__(self)
        self.url = url_
        self.header = header_
        self.db = db_
        self.collection = collection_ 
        self.keys = keys_

    def run(self):
        db = self.db
        collection = self.collection 
        while True:
            sensor1Data = json.loads(requests.get(self.url, headers=self.header).text)["deviceSensors"]
            threadLock.acquire() 
            print("Acquired the lock")
            sensor1Occupied = jsonBool(next((x for x in sensor1Data if x["reference"] == "carDetected"), None)["value"])
            sensor1ParkingDuration = float(next((x for x in sensor1Data if x["reference"] == "parkingDuration"), None)["value"])
            sensor1Reserved = jsonBool(collection.find_one({'id':'test1'})["reserved"])
            print(sensor1Occupied)
            print(sensor1Reserved)
            print(sensor1ParkingDuration)
            collection.update({'id':'test1'},{'$set':{'occupied': sensor1Occupied, 'parkingDuration':sensor1ParkingDuration, 'light': calculateLight(sensor1Reserved, sensor1Occupied)}})

            threadLock.release()
            print("Let go of the lock")
            time.sleep(60)

class reserveThread(threading.Thread):
    def __init__(self, url_, header_, db_, collection_, keys_):
        threading.Thread.__init__(self)
        self.url = url_
        self.header = header_ 
        self.db = db_
        self.collection = collection_
        self.keys = keys_

    def run(self):
        collection = self.collection
        while True:
            '''
            #get the request
            reserveSpotID = ""
            #query the key value using the spot ID and station name. 
            #collection = self.db["reserveStation"]
            #querySpot = json.loads(collection.find_one({'id':reserveSpotID})
            reserveTime = ""
            reserveDuration = ""
            '''
            querySpot = collection.find_one({'id':'test1'}) 
            occupied = querySpot["occupied"]   
            reserved = querySpot["reserved"]
            #reserved = True

            if not occupied and not reserved: 

                threadLock.acquire()
                print("Acquired lock")
                print("Turning on the light")
                req = requests.post(self.url, data={'command':'ON'})
                collection.update({'id':'test1'},{'$set':{'reserved': True}})
                print(req)
                print("Doing shit")  
            
                threadLock.release() 
                print("Released lock")

            else:
                print("It's already reserved/occupied!")
            time.sleep(1000)

def jsonBool(jsonbond):
    return jsonbond == 'true'

def calculateLight(reserved, occupied):

    if occupied:
        return 0
    elif reserved:
        return 2
    elif not occupied:
        return 1

#client = MongoClient()
client = MongoClient("mongodb://db:27017")
db = client.parkingDatabase
collection = db.testStation1


test1 = 'axsense_TEC_Labor'
#Key-value pair for easy querying 
devToSpot = {test1: 'test1', 'sensor2': 'test2', 'sensor3': 'test3', 
        'sensor4': 'test4', 'sensor5': 'test5'}

pprint.pprint(collection.find_one({"id":devToSpot[test1]}))

sensor1Url = 'https://api-sbb.wolkabout.com/api/devices/70B3D54995B37FEA'
sensor1Token = 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIyIiwiYXV0aCI6WyJVU0VSX1JFQUQiLCJVU0VSX1VQREFURSIsIlVTRVJfQ1JFQVRFIiwiVVNFUl9ERUxFVEUiLCJSVUxFX1JFQUQiLCJSVUxFX1VQREFURSIsIlJVTEVfQ1JFQVRFIiwiUlVMRV9ERUxFVEUiLCJERVZJQ0VfUkVBRCIsIkRFVklDRV9VUERBVEUiLCJERVZJQ0VfQ1JFQVRFIiwiREVWSUNFX0RFTEVURSIsIkRFVklDRV9UWVBFX1JFQUQiLCJERVZJQ0VfVFlQRV9VUERBVEUiLCJERVZJQ0VfVFlQRV9DUkVBVEUiLCJERVZJQ0VfVFlQRV9ERUxFVEUiLCJST0xFX1JFQUQiLCJST0xFX1VQREFURSIsIlJPTEVfQ1JFQVRFIiwiUk9MRV9ERUxFVEUiLCJEQVNIQk9BUkRfUkVBRCIsIkRBU0hCT0FSRF9VUERBVEUiLCJEQVNIQk9BUkRfQ1JFQVRFIiwiREFTSEJPQVJEX0RFTEVURSIsIlJFUE9SVF9SRUFEIiwiUkVQT1JUX1VQREFURSIsIlJFUE9SVF9DUkVBVEUiLCJSRVBPUlRfREVMRVRFIiwiUE9JTlRfUkVBRCIsIlBPSU5UX1VQREFURSIsIlBPSU5UX0NSRUFURSIsIlBPSU5UX0RFTEVURSIsIk5PVElGSUNBVElPTl9SRUFEIiwiTU9CSUxFX1JFQUQiLCJURU1QTEFURV9SRUFEIiwiVEVNUExBVEVfVVBEQVRFIiwiVEVNUExBVEVfQ1JFQVRFIiwiVEVNUExBVEVfREVMRVRFIl0sImNvbnRleHQiOjEsInJvbGUiOjIsImV4cCI6MTU0NDEwMTcxM30.v5OmQcdMSeX_nx4NzUVhnLyBFZbm0_3jllhlZPN_wRScziZnbrgzg9_i26Pagfbme6jNLpv4h6Y5m5WMQygrTA'
sensor1Head = {'Authorization': 'Bearer {}'.format(sensor1Token), 'Accept': '*/*'}
reserve1Url = 'https://iot-starterkit-kd-iot.app.sbb-aws.net/downlink/message?deviceId=70B3D5E75E0036AB'
reserve1Head = {'':''}
print("initialized query sensor")
threadLock = threading.Lock()
sensorDR1 = sensorThread(sensor1Url, sensor1Head, db, collection, devToSpot)
reserve1 = reserveThread(reserve1Url, reserve1Head, db, collection, devToSpot)
sensorDR1.start()
reserve1.start() 

