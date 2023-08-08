from pymongo import MongoClient 
from .mongo_db_configs import mongo_db_infos

# Classe de conexão
class DBConnectionHandler:
    # criando a string de conexão
    def __init__(self):
        self.__connection_string = 'mongodb://{}:{}/'.format(
            mongo_db_infos["HOST"],
            mongo_db_infos["PORTA"]
        )
        self.__database_name = mongo_db_infos["BD_NAME"]
        self.__client = None
        self.__db_connection = None

    # conexão banco
    def connect_to_db(self):
        self.__client = MongoClient(self.__connection_string)
        self.__db_connection = self.__client[self.__database_name]
    
    def get_db_connection(self):
        return self.__db_connection
    
    def get_db_client(self):
        return self.__client
     