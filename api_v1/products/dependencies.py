from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends,Path
from fastapi import HTTPException
from core.models.products import ProductModel
from api_v1.products import crud
from core.models import db_helper



async def product_by_id(product_id: Annotated[int, Path], db: AsyncSession = Depends(db_helper.db_helper.get_db)) -> ProductModel:
    product = await crud.get_product(db=db, product_id=product_id)
    if product is not None:
        return product
    else:
        raise HTTPException(status_code=404, detail="Not found")