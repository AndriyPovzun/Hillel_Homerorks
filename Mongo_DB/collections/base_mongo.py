from Mongo_DB.db_connector.connection import my_collection


class BaseDB:
    def __init__(self):
        self._collection = my_collection

    def _insert_one(self, item: dict):
        self._collection.insert_one(item)

    def _insert_many(self, dictionaries: list):
        self._collection.insert_many(dictionaries)

    def _get_all(self):
        result = self._collection.find({}, {'_id': 0})
        return result

    def _get_by(self, attribute: dict):
        results = self._collection.find(attribute)
        return results

    def _get_one(self):
        results = self._collection.find_one()
        for result in results:
            return result

    def _get_one_by(self, attribute, value):
        result = self._collection.find_one({attribute: value}, {'_id': 0})
        return result

    def _delete_one(self, attribute, value):
        self._collection.delete_one({attribute: value})

    def _delete_many(self, dictionaries: list):
        self._collection.delete_many(dictionaries)

    def _update_one(self, condition: dict, set_value: dict):
        self._collection.update_one(condition, set_value)

    def _update_many(self, dictionaries: list):
        self._collection.update_many(dictionaries)
