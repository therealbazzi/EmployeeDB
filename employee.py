from typing import Text
from redis_om import (Field, HashModel)
from redisearch.client import TagField

class Employee(HashModel):
    firstName: str = Field(index=True)
    lastName: str = Field(index=True)
    salary: int = Field(index=True)
    department: str = Field(index=True)
    isAdmin: int = Field(index=True)




