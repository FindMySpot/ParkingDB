from flask import Flask, jsonify
from flask_cors import CORS
import os
import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://db:27017')
db = client.parkingDatabase


app = Flask(__name__)
CORS(app)

@app.route('/availability/<string:station>',methods=['GET'])
def get_station_availability(station):
    stationList = station.split('#')
    print(stationList)
    resultList = []
    for stationName in stationList:
        resultList.append({stationName: db.stationName.find({'occupied':'false','reserved':'false'}).count()})
    
    return(jsonify(resultList))   

if __name__ == '__main__':
    app.run(debug=True)

        
