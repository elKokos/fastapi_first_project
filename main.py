from fastapi import Depends, FastAPI
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
	await delete_tables()
	print("base is clean")
	await create_tables()
	print("base is ready")
	yield
	print("off")
 

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)


