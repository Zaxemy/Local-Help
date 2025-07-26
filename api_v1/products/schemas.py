from pydantic import BaseModel


class CreateProduct(BaseModel):
    name: str
    price: int
    description: str

class ResponseProduct(CreateProduct):
    id: int

class UpdateProduct(CreateProduct):
    name: str | None = None 
    price: int | None = None
    description: str | None = None

