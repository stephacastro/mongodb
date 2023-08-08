from typing import Dict, List
from bson.objectid import ObjectId
from datetime import timedelta

class MinhaCollectionRepository:
    def __init__(self, db_connection):
        self.__collection_name = "minhaCollection"
        self.__db_connection = db_connection
        
    def insert_document(self, document: Dict) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)
        return document
    
    def insert_list_of_documents(self, list_of_documents: List[Dict]) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_many(list_of_documents)
        return list_of_documents

    def select_many(self, filtro) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(filtro,  # filtrando dado especifico
                               {"endereco": 0, "_id": 0} # Opções de retorno (possibilidade de escolher dados que não precisam ser vistos)   
                               )
        data2 = collection.find({}) # filtrando todos os documentos 

        response = []

        for elemento in data: response.append(elemento)
        return response 
    
    def select_one(self, filtro) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find_one(filtro, {"_id": 0})
        return response
    
     # retornando uma propriedade existente 
    def select_if_property_exists(self):
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find({"endereco": {"$exists": True}})
        
        for elemento in data:
            print(elemento)

    # ordenação (crescente ou decrescente)
    def select_many_order(self):
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find({"nome": "Stephanie"},  # filtrando dado especifico
                               {"endereco": 0, "_id": 0} # Opções de retorno (possibilidade de escolher dados que não precisam ser vistos)   
                               ).sort([{"pedidos.pizza", -1}])
        
        for elemento in data:
            print(elemento)

    # adicionando condições
    def select_or(self):
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find({"$or": [{"nome": "Stephanie"}, {"Hello": {"$exists": True}}]})
        
        for elemento in data:
            print(elemento)

    # busca por _id
    def select_object_id(self):
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find({"_id": ObjectId("64cae6ca78f7fd9cad0bba6f")})
        
        for elemento in data:
            print(elemento)
    
    # editando/update de registros 
    def edit_registry(self):
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.update_one({"_id": ObjectId("64cc45effdadf3f842685e98")}, # filtro
                              {"$set": {"nome": "Manuela Castro"}} # update
                              )
        print(data.modified_count) # mostra quantos elementos foram modificados

    # editando/update varios registros  
    def edit_many_registries(self):
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.update_many({"profissao": "Porgramador"}, # filtro
                              {"$set": {"profissao": "Desenvolvedor"}} # update / edição
                              )
        print(data.modified_count) # mostra quantos elementos foram modificados

    def edit_many_registries_2(self, filtro, update):
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.update_many(filtro, # filtro
                              {"$set": update} # update
                              )
        print(data.modified_count) # mostra quantos elementos foram modificados
    
    # incrementando um registro 
    def edit_many_increment(self, num):
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.update_many({"_id": ObjectId("64cc488b1a0be4dd9996a687")}, # filtro
                              {"$inc": {"idade": num}} # incremento
                              )
        print(data.modified_count) # mostra quantos elementos foram modificados

    # deletando 
    def delete_registries(self):
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.delete_many({"nome": "Stephanie"}) # filtro

        print(data.deleted_count)

    def delete_registry(self):
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.delete_one({"_id": ObjectId("64b87fcec09baddf7b2e5aa4")}) # filtro

        print(data.deleted_count)

    # index ttl delete um registro que tem como propriedade o index criado no tempo determinado
    def create_index_ttl(self):
        collection = self.__db_connection.get_collection(self.__collection_name)
        tempo_de_vida = timedelta(seconds=10) # determinando o tempo que o banco exluirá apos a criação do regristro
        collection.create_index("data_de_criacao", expireAfterSeconds=tempo_de_vida.seconds) # cria i index ttl  