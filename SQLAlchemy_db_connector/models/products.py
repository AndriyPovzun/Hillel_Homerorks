from SQLAlchemy_db_connector.db_connector.connector import Base
from sqlalchemy import Column, VARCHAR, INTEGER
from sqlalchemy.orm import relationship


class Products(Base):
    __tablename__ = 'products'
    id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR(25))
    price = Column(INTEGER)

    orders = relationship("Orders", back_populates="products")

    def __str__(self):
        return f'id: {self.id}, name: {self.name}, price: {self.price}'
