from RestplusAPI.database import db
from RestplusAPI.database.dtos import Product

def create_product(data):
    name = data.get('name')
    product = Product(name)
    db.add(product)
