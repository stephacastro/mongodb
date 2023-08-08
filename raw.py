from pymongo import MongoClient

connection_string = "mongodb://localhost:27017/" # stringo de conexão

client = MongoClient(connection_string) # conexão com o Mongo
db_connection = client['bd'] # conexão com o bd

print(db_connection)

collection = db_connection.get_collection("minhaCollection") # acessando a coleção

print(collection)

# filtrando

search_filter = {"ola":"mundo"} 

search_filter_2 = {"estou":"aqui"} 

print(collection.find_one())

print(collection.find(search_filter))

for registro in search_filter:
    print(search_filter)


for registro in search_filter_2:
    print(search_filter_2)


# Inserindo dados

collection.insert_one({
    "Estou":"Inserindo registros",
    "Numeros":[123, 456, 789]
})