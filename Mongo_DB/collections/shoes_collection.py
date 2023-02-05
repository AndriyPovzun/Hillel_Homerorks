from Mongo_DB.collections.base_mongo import BaseDB


class ShoesCollection(BaseDB):
    def __init__(self):
        super().__init__()

    def get_by_brand(self, brand: str):
        result = self._get_by({'brand': brand})
        return result

    def get_by_model(self, model: str):
        result = self._get_by({'model': model})
        return result

    def get_by_price(self, price: str):
        result = self._get_by({'price': price})
        return result

    def find_first_by(self, attribute, value):
        result = self._get_one_by(attribute, value)
        return result

    def get_all_shoes(self):
        result = self._get_all()
        return result

    def insert_shoes(self, brand: str, model: str, price: int):
        self._insert_one({'brand': brand, 'model': model, 'price': price})

    def insert_many_shoes(self, list_of_shoes: list):
        self._insert_many(list_of_shoes)

    def delete_one_by(self, attribute, value):
        self._delete_one(attribute, value)

    def update(self, condition: dict, set_value: dict):
        self._update_one(condition, set_value={"$set": set_value})
