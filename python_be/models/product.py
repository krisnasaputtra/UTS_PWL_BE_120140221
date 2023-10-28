from sqlalchemy import Column, Integer, Text
from .meta import Base

class Product(Base):
    """ The SQLAlchemy declarative model class for a Product object. """
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    price = Column(Integer, nullable=False)
    stock = Column(Integer, nullable=False)

    def to_dict(self):
        """ Return a dictionary representation of a Product object. """
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'stock': self.stock,
        }