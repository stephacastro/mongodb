'''
db_handler = DBConnectionHandler()
conn1 = db_handler.get_db_connection()
print(conn1) # vai retornar None

print('-'*100)

db_handler.connect_to_db()
conn2 = db_handler.get_db_connection()
print(conn2) # vai retornar a conexão

collection = conn2.get_collection('minhaCollection')

collection.insert_one({
    "Hello":"World",
    "Numeros":[165, 454, 195]
})

pedido = {
    "nome": "Stephanie",
    "endereco": "Rua do exemplo",
    "pedidos": {
        "pizza": 3,
        "x-salada": 5
    } 
}

minha_collection_repository.insert_document(pedido)

list_of_documents = [
    {"Xuxa": "Meneguel"},
    {"Cantora": "Anitta"},
    {"Sheldon": "Cooper"},
    {"Yuri": "Alberto"}
]

minha_collection_repository.insert_list_of_documents(list_of_documents)
'''


from models.connection_options.connection import DBConnectionHandler
from models.connection_options.repository.minhaCollection_repository import MinhaCollectionRepository
from datetime import datetime, timedelta

db_handler = DBConnectionHandler()
db_handler.connect_to_db()
db_connection = db_handler.get_db_connection()

minha_collection_repository = MinhaCollectionRepository(db_connection)

response = minha_collection_repository.select_many({"nome": "Stephanie", "pedidos.pizza": 1})
#print(response)
#print()

#response2 = minha_collection_repository.select_one({"nome": "Stephanie"})
#print(response2)

#minha_collection_repository.select_if_property_exists()

#minha_collection_repository.select_many_order()

#minha_collection_repository.select_or()

#minha_collection_repository.select_object_id()

'''
minha_collection_repository.insert_document({"nome": "Pedro",
                          "apelido": "Pedrin",
                          "profissao": "Porgramador"})
'''


#filtro = {"nome": "Murilo"}
#update = {"idade": 30}
#update = {"idade": 25} # add uma nova proriedade
'''update = {"endereco": {
                "cep": "0942833",
                "rua": "do exemplo",
                "bairro": "dos bairros"
}}'''

#minha_collection_repository.edit_many_registries_2(filtro, update)

#minha_collection_repository.edit_many_registries()

#minha_collection_repository.edit_many_increment(3)
#minha_collection_repository.edit_many_increment(-2)

#minha_collection_repository.delete_registries()

#minha_collection_repository.delete_registry()


#minha_collection_repository.create_index_ttl()

documento = {"nome": "Marcos", "Idade": 30, "data_de_criacao": datetime.utcnow() -timedelta(hours=3)}
minha_collection_repository.insert_document(documento)