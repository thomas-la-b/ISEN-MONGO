#-----------------------------
# Cloud Computing
# Projet 1 Ex 4
# SOETENS Gatien BRUFAU Thomas
#-----------------------------

# Import des modules
import pymongo
from pymongo import MongoClient

# Connexion au cluster
cluster=MongoClient("mongodb+srv://Gatens:test1234@cluster0.sppia.mongodb.net/bycicle_services?retryWrites=true&w=majority")
db=cluster["bycicle_services"]
collection=db["Lille"]

#recherche une station par un nom (quelques lettres)
def findStation(recherche):
    result = collection.find({"fields.nom":{"$regex": recherche, "$options":'i'}})
    for i in result:
        print(i)

#findStation("militaire")

# Update a station
def update(station):
    collection.update_one(
        {"fields.nom":station},
        {'$set': {'fields.etat':'HORS SERVICE'}} # passe l'etat de la station a hors service
    )

#update("N.D. DE LA TREILLE")
# Remove station and data
def remove(station):
    query={"fields.nom":station}
    collection.delete_one(query)

#remove("N.D. DE LA TREILLE")

# Deactivate all stations in an area
def deactivate(): #put stations around a polygon in state : HORS SERVICE
    result = collection.find({"geometry": { 
    "$near" : {
        "$geometry": {
            "type": "Polygon",
            "coordinates":[ 3.0629778380918538 ,50.64105303104528]
            },
        "$maxDistance": 300,
        "$minDistance": 0
}
}})
    for i in result:
        update(i["fields"]["nom"])
        print(i)

deactivate()