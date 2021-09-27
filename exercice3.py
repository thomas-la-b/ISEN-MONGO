#-----------------------------
# Cloud Computing
# Projet 1 Ex 3
# SOETENS Gatien BRUFAU Thomas
#-----------------------------

# Import des modules
import pymongo
from pymongo import MongoClient

# Connexion au cluster
cluster=MongoClient("mongodb+srv://Gatens:test1234@cluster0.sppia.mongodb.net/bycicle_services?retryWrites=true&w=majority")
db=cluster["bycicle_services"]

collection = db["Lille"]

loc= [ 50.64105303104528, 3.0629778380918538]

result = collection.find({"geometry": { 
    "$near" : {
        "$geometry": {
            "type": "Point",
            "coordinates":[ 3.0629778380918538 ,50.64105303104528]
            },
        "$maxDistance": 300,
        "$minDistance": 0
}
}})

for i in result:
    print(i)