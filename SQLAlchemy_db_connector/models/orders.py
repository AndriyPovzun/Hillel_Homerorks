from SQLAlchemy_db_connector.db_connector.connector import Base
from sqlalchemy import Column, INTEGER
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Orders(Base):
    __tablename__ = 'orders'
    id = Column(INTEGER, primary_key=True)
    product_id = Column(INTEGER, ForeignKey('products.id'), nullable=False)
    quantity = Column(INTEGER, nullable=False)

    products = relationship("Products", back_populates="orders")

    def __str__(self):
        return f'order_id: {self.id}, product_id: {self.product_id}, quantity: {self.quantity} '
