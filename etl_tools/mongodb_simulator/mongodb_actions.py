import pymongo
import random

class MongoDBActions:
    def __init__(self, uri, database_name, collection_name, document):
        self.uri = uri
        self.database_name = database_name
        self.collection_name = collection_name
        self.document = document

    def get_random_document(self):
        client = pymongo.MongoClient(self.uri)
        db = client[self.database_name]
        collection = db[self.collection_name]
        random_document = collection.find_one({}, {'_id': 1})
        client.close()
        if random_document:
            return random_document['_id']
        else:
            return None

    def create_document(self):
        client = pymongo.MongoClient(self.uri)
        db = client[self.database_name]
        collection = db[self.collection_name]
        data = self.document
        collection.insert_one(data)
        client.close()
        
    def update_document(self, percent_to_update=10, default_quantity=None):
        client = pymongo.MongoClient(self.uri)
        db = client[self.database_name]
        collection = db[self.collection_name]

        random_id = self.get_random_document()

        if random_id:
            random_document = collection.find_one({'_id': random_id})

            if random_document:
                document_keys = list(random_document.keys())
                document_keys.remove('_id')

                if default_quantity is None:
                    num_keys_to_update = len(document_keys) * percent_to_update // 100
                    num_keys_to_update = max(num_keys_to_update, 1)
                else:
                    num_keys_to_update = min(default_quantity, len(document_keys))

                keys_to_update = random.sample(document_keys, num_keys_to_update)

                update_data = {}

                for key in keys_to_update:
                    value_to_update = self.document.get(key)
                    update_data[key] = value_to_update

                collection.update_one({'_id': random_id}, {'$set': update_data})

        client.close()

    def delete_document(self):
        client = pymongo.MongoClient(self.uri)
        db = client[self.database_name]
        collection = db[self.collection_name]

        random_id = self.get_random_document()

        if random_id:
            collection.delete_one({'_id': random_id})

        client.close()





