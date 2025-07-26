from fastapi import APIRouter, HTTPException, Depends
from api_v1.products import crud
from api_v1.products.schemas import CreateProduct, ResponseProduct, UpdateProduct, DeleteProduct
from sqlalchemy.ext.asyncio import AsyncSession
from core.models.db_helper import db_helper
from core.models.products import ProductModel
from api_v1.products.dependencies import product_by_id


router = APIRouter(prefix="/products")


@router.get("/", response_model=list[ResponseProduct])
async def get_products(db: AsyncSession = Depends(db_helper.get_db)):
    return await crud.get_products(db=db)


@router.post("/", response_model=ResponseProduct)
async def create_products(product_schema: CreateProduct, db: AsyncSession = Depends(db_helper.get_db)):
    return await crud.create_product(db, product_schema=product_schema)


@router.get("/{product_id}/", response_model=ResponseProduct)
async def get_product(product = Depends(product_by_id)):
    return product
    
@router.put("/{product_id}/")
async def update_product(update_product: UpdateProduct, product: ProductModel = Depends(product_by_id), db: AsyncSession = Depends(db_helper.get_db)):
    return await crud.update_product(db=db, product=product,update_product=update_product)

@router.delete("/{product_id}/")
async def delete_product(product: ProductModel = Depends(product_by_id), db: AsyncSession = Depends(db_helper.get_db)):
    await crud.delete_product(db=db,product=product)