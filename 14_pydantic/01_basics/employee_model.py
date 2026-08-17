from typing import Optional
from pydantic import BaseModel, Field
import re

class Empoyee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length = 3,
        max_length = 50,
        description = "Employee name",
        examples = "Harsh"
    )
    department: Optional[str] = 'General'
    salary: float = Field(
        ...,
        ge=10000, # greater than equal to
        le=100000,
        description= "annual salary in usd"
    )

class User(BaseModel):
    email: str = Field(
        ...,
        regex=r''
    )
    phone: str = Field(
        ...,
        regex=r''
    )
    age: int = Field(
        ...,
        ge = 0,
        le = 110,
        description = "age in years"
    )
    discount: float = Field(
        ...,
        ge = 0,
        le = 100,
        description = "discount percentage"
    )