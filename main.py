from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn
from core.models.base import Base
from sqlalchemy.ext import asyncio
from core.models.db_helper import db_helper
from api_v1.products.views import router as ProductRouter


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(ProductRouter)



if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8888, reload=True)
