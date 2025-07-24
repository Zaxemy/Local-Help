from fastapi import APIRouter, HTTPException, Depends
from api_v1.products import crud
from api_v1.products.schemas import CreateProduct, ResponseProduct
from sqlalchemy.ext.asyncio import AsyncSession
from core.models.db_helper import db_helper


router = APIRouter(prefix="/products")


@router.get("/", response_model=list[ResponseProduct])
async def get_products(db: AsyncSession = Depends(db_helper.get_db)):
    return await crud.get_products(db=db)


@router.post("/", response_model=ResponseProduct)
async def create_products(product_schema: CreateProduct, db: AsyncSession = Depends(db_helper.get_db)):
    return await crud.create_product(db, product_schema=product_schema)


@router.get("/{product_id}/", response_model=ResponseProduct)
async def get_product(product_id: int, db: AsyncSession = Depends(db_helper.get_d-b)):
    product = await crud.get_product(db=db, product_id=product_id)
    if product is not None:
        return product
    else:
        raise HTTPException(status_code=404, detail="Not found")
