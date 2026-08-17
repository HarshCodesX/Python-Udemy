from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True

product_one = Product(id=1, name="Laptop", price=88.97, in_stock=True)

product_two = Product(id=2, name="mouse", price=48.77)

# product_three = Product(name="keyboard") # this will throw error