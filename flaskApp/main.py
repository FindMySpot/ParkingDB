from flask import Flask, jsonify
from flask_cors import CORS
import requests
import os
import datetime
import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://db:27017')
db = client.parkingDatabase

app = Flask(__name__)
CORS(app)


@app.route('/availability/<string:station>',methods=['GET'])
def get_station_availability(station):
    stationList = station.split('#')
    #print(stationList)
    resultList = []
    for stationName in stationList: 
        count = 0
        for item in db[stationName].find({'occupied':False,'reserved':False}):
            count = count + 1
        resultList.append({stationName: count})
    
    return(jsonify(resultList))   

@app.route('/populate', methods=['GET'])
def populate():
    db.testStation1.insert_many([{"id" : "test0", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test1", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test2", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test3", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test4", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test5", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test6", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test7", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test8", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test9", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}])
    db.testStation2.insert_many([{"id" : "test0", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test1", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test2", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test3", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test4", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test5", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test6", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test7", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test8", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test9", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}])
    db.testStation3.insert_many([{"id" : "test0", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test1", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test2", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test3", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test4", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test5", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test6", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test7", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test8", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test9", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}])
    db.testStation4.insert_many([{"id" : "test0", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test1", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test2", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test3", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test4", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test5", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test6", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test7", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test8", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test9", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}])
    db.testStation5.insert_many([{"id" : "test0", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test1", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test2", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test3", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test4", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test5", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test6", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test7", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test8", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test9", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}])
    db.testStation6.insert_many([{"id" : "test0", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test1", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test2", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test3", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test4", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test5", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test6", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test7", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test8", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test9", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}])
    db.testStation7.insert_many([{"id" : "test0", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test1", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test2", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test3", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test4", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test5", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test6", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test7", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test8", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test9", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}])
    db.testStation8.insert_many([{"id" : "test0", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test1", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test2", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test3", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test4", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test5", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test6", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test7", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test8", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test9", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}])
    db.testStation9.insert_many([{"id" : "test0", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test1", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test2", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test3", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test4", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test5", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test6", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test7", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test8", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test9", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}])
    db.testStation10.insert_many([{"id" : "test0", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test1", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test2", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test3", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test4", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test5", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test6", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test7", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test8", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test9", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}])
    db.testStation11.insert_many([{"id" : "test0", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test1", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test2", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test3", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test4", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test5", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test6", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test7", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test8", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test9", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}])
    db.testStation12.insert_many([{"id" : "test0", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test1", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test2", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test3", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test4", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test5", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test6", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test7", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test8", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test9", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}])
    db.testStation13.insert_many([{"id" : "test0", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test1", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test2", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test3", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test4", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test5", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test6", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test7", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test8", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test9", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}])
    db.testStation14.insert_many([{"id" : "test0", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test1", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test2", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test3", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test4", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test5", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test6", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test7", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test8", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test9", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}])
    db.testStation15.insert_many([{"id" : "test0", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test1", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test2", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test3", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test4", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test5", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test6", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test7", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test8", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test9", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}])
    db.testStation16.insert_many([{"id" : "test0", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test1", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test2", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test3", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test4", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test5", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test6", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test7", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test8", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}, {"id" : "test9", "occupied" : False, "reserved" : False, "rTimes" : [ ], "light" : 1, "parkingDuration" : 0, "rDuration" : 0, "parkingStart" : datetime.datetime.utcnow()}])
    return(True)

if __name__ == '__main__':
    app.run(debug=True)

#epoch, minutes, dt
def dtToEpoch(dt):
    return((dt - datetime.datetime(1970,1,1)).total_seconds())

def resHelper(newtime, newdurt, oldtime):
    oldepoch = dtToEpoch(oldtime)
    return((newtime + 60*newdurt) > oldepoch)

def epochToDt(ep):
    return datetime.datetime.fromtimestamp(newtime)

@app.route('/reserve/<float:rtime>/duration/<int:dur>/station/<string:station>', methods=['POST'])
def make_reservation(rtime, dur, stationName):
    spotList = db.stationName.find({'occupied':False,'reserved':False})
    for spot in spotList:
        for reservedSlot in spot:
            if(resHelper(rtime, dur, reservedSlot["date"])):
                db.stationName.update({'id':spot['id']},{'$push':{'rTimes':{'date':epochToDt(rtime), 'duration':dur}}})
                db.stationName.update({'id':spot['id']},{'$set':{'reserved':True}})
                print("reservation success!")
                return True
    print("reservation failed!")
    return False
       
@app.route('/reserveone', methods=['POST'])
def make_oneres():
    switchUrl = 'https://iot-starterkit-kd-iot.app.sbb-aws.net/downlink/message?deviceId=70B3D5E75E0036AB'
    switchData = {'command':'ON'}
    reply = requests.post(switchUrl, data=switchData)
    print(reply)
    return "SUCCESS"

@app.route('/cancelone', methods=['POST'])
def cancel_oneres():
    switchUrl = 'https://iot-starterkit-kd-iot.app.sbb-aws.net/downlink/message?deviceId=70B3D5E75E0036AB'
    switchData = {'command':'OFF'}
    reply = requests.post(switchUrl, data=switchData)
    print(reply) 
    return "SUCCESS"
