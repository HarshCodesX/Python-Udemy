from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address

address = Address(
    street = "123 adress",
    city="jaipur",
    postal_code="83838"
)

user = User(
    id=1,
    name="harsh",
    address=address
)

user_data = {
    "id": 1,
    "name": "harsh",
    "address": {
        "street": "123abc",
        "city": "Paris",
        "postal_code": "33778"
    }
}

user = User(**user_data)
print(user)