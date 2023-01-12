from SQLAlchemy_db_connector import connection_db
from SQLAlchemy_db_connector.models.orders import Orders
from SQLAlchemy_db_connector.models.products import Products
from sqlalchemy import select, delete, update


class ProductsRepository:
    def __init__(self):
        self.__session = connection_db.session
        self.__result_list = []

    def get_by_id(self, id_value: int) -> str:
        product = self.__session.get(Products, {'id': id_value})
        return product

    def get_all(self) -> list:
        all_products = self.__session.query(Products).all()
        return all_products

    def insert_product(self, product: Products):
        self.__session.add(product)

    def get_by_name(self, name_value: str) -> str:
        query = select(Products).where(Products.name == name_value)
        result = self.__session.scalar(query)
        return result

    def delete_product_by_id(self, id_value: int):
        self.__session.execute(delete(Products).where(Products.id == int(id_value)))

    def update_product_price_by_id(self, id_value: int, price: int):
        self.__session.execute(update(Products).where(Products.id == id_value).values(price=price))

    def update_product_name_by_id(self, id_value: int, name: str):
        self.__session.execute(update(Products).where(Products.id == id_value).values(name=name))

    def __parse_joined_products_orders_data(self, sequence: [Products, Orders]) -> str:
        for row in sequence:
            self.__result_list.append(f'{row[0]}, {row[1]}')
        result = '\n'.join(self.__result_list)
        return result

    def get_data_from_products_and_users(self) -> str:
        rows = self.__session.execute(select(Products, Orders).join(Orders.products))
        result = self.__parse_joined_products_orders_data(rows)
        return result

    def get_data_from_products_and_users_by_order_id(self, order_id_value: int) -> str:
        rows = self.__session.execute(select(Products, Orders).join(Orders.products).where(Orders.id == order_id_value))
        result = self.__parse_joined_products_orders_data(rows)
        return result
