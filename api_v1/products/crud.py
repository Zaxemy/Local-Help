from sqlalchemy.ext.asyncio import AsyncSession
from core.models.products import ProductModel
from api_v1.products.schemas import (
    ResponseProduct,
    CreateProduct,
    UpdateProduct,
    
)
from sqlalchemy import select


async def get_products(db: AsyncSession):
    stmt = select(ProductModel).order_by(ProductModel.id)
    result = await db.execute(stmt)
    products = result.scalars().all()
    return products


async def get_product(
    db: AsyncSession,
    product_id: int,
):
    return await db.get(ProductModel, product_id)


async def create_product(db: AsyncSession, product_schema: CreateProduct):
    product = ProductModel(**product_schema.model_dump())
    db.add(product)
    await db.commit()
    await db.refresh(product)
    return product


async def update_product(
    db: AsyncSession,
    update_product: UpdateProduct,
    product: ProductModel,
):
    for name, value in update_product.model_dump(exclude_unset=True).items():
        setattr(product, name, value)
    db.add(product)
    await db.commit()
    await db.refresh(product)
    return product


async def delete_product(
    db: AsyncSession,
    product: ProductModel,
):
    db.delete(product)
    db.commit()        