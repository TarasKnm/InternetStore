from sqlalchemy import DECIMAL, Column, Integer, ForeignKey, VARCHAR
from sqlalchemy.orm import relationship

from ..db.base_class import Base

class ProductCategory(Base):
    __tablename__ = 'product_categories'
    
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(45))
    description = Column(VARCHAR(180))
    
    products = relationship("Product", back_populates="product_category")

class ProductInventory(Base):
    __tablename__ = 'product_inventories'
    
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    
    products = relationship("Product", back_populates="product_inventory")

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(45))
    description = Column(VARCHAR(180))
    price = Column(DECIMAL)
    quantity = Column(Integer,default=0)
    product_category_id = Column(Integer, ForeignKey(ProductCategory.id))
    product_inventory_id = Column(Integer, ForeignKey(ProductInventory.id))
    
    product_category = relationship('ProductCategory', back_populates='products')
    product_inventory = relationship('ProductInventory', back_populates='products')