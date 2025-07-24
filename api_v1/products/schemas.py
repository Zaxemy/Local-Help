from pydantic import BaseModel


class CreateProduct(BaseModel):
    name: str
    price: int
    description: str

class ResponseProduct(CreateProduct):
    id: int
