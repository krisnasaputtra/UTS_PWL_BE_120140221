from sqlalchemy import Column, Integer, Text
from .meta import Base

class Cart(Base):
    """ The SQLAlchemy declarative model class for a Cart object. """
    __tablename__ = 'carts'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    price = Column(Integer, nullable=False)
    buy_amount = Column(Integer, nullable=False)
    total_price = Column(Integer, nullable=False)

    def to_dict(self):
        """ Return a dictionary representation of a Cart object. """
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'buy_amount': self.buy_amount,
            'total_price': self.total_price
        }