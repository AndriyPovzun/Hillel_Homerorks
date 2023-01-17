from SQLAlchemy_db_connector import connection_db
from SQLAlchemy_db_connector.models.orders import Orders
from SQLAlchemy_db_connector.models.products import Products
from sqlalchemy import select, delete, update


class OrdersRepository:
    def __init__(self):
        self.__session = connection_db.session
        self.__result_list = []

    def get_all_orders(self) -> list:
        all_orders = self.__session.query(Orders).all()
        return all_orders

    def get_by_id(self, id_value: int):
        result = self.__session.get(Orders, {"id": id_value})
        return result

    def insert_order(self, order: Orders):
        self.__session.add(order)

    def delete_by_id(self, order_id: int):
        self.__session.execute(delete(Orders).where(Orders.id == int(order_id)))

    def __parse_joined_products_orders_data(self, sequence: [Products, Orders]) -> str:
        for row in sequence:
            self.__result_list.append(f'{row[0]}, name: {row[1].name}, price: {row[1].price}')
        result = '\n'.join(self.__result_list)
        return result

    def get_orders_with_name_and_price(self) -> str:
        all_orders = self.__session.execute(select(Orders, Products).join(Products.orders))
        result = self.__parse_joined_products_orders_data(all_orders)
        return result

    def update_order_quantity_by_id(self, order_id: int, quantity_value: int):
        self.__session.execute(update(Orders).where(Orders.id == order_id).values(quantity=quantity_value))
