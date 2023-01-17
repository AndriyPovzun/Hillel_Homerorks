from SQLAlchemy_db_connector.repositories.products_repository import ProductsRepository
from SQLAlchemy_db_connector.repositories.orders_repository import OrdersRepository
from random import randint
from SQLAlchemy_db_connector.models.orders import Orders
from SQLAlchemy_db_connector.models.products import Products

product_repo = ProductsRepository()
orders_repo = OrdersRepository()
"""
Get user from DB by ID
"""
# result = product_repo.get_by_id(7)
# print(result)

"""
Test deleting user from DB
"""
# product_repo.delete_product_by_id(7)

"""
Get all products from DB
"""

# all_products = product_repo.get_all()
# for product in all_products:
#     print(product)

"""
Test update product price
"""
# print(product_repo.get_by_name('Nike React 87'))
# product_repo.update_product_price_by_id(id_value=4, price=210)
# print(product_repo.get_by_id(id_value=4))

"""
Test insert product 
"""
# product_repo.insert_product(Products(name="Test Shoes", price=999))
"""
Test delete product
"""
# product_repo.delete_product_by_id(8)
"""
Test get with JOIN
"""
# products = product_repo.get_data_from_products_and_users()
# print(products)
"""
Test get with JOIN
"""
# print(product_repo.get_data_from_products_and_users_by_order_id(order_id_value=5))

"""
Test get all records from orders table
"""
# all_orders = orders_repo.get_all_orders()
# for order in all_orders:
#     print(order)

"""
Test get order by ID
"""
# print(orders_repo.get_by_id(id_value=3))

"""
Test insert new record in orders table
"""
# orders_repo.insert_order(Orders(product_id=randint(1, 5), quantity=randint(1, 20)))
"""
Test delete record from orders
"""
# orders_repo.delete_by_id(order_id=6)

"""
Test get orders with name and price from products table
"""
# print(orders_repo.get_orders_with_name_and_price())

"""
Test update order record
"""
# orders_repo.update_order_quantity_by_id(order_id=5,quantity_value=15)
