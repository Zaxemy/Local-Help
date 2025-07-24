from sqlalchemy.ext.asyncio import AsyncSession
from core.models.products import ProductModel
from api_v1.products.schemas import ResponseProduct, CreateProduct
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
