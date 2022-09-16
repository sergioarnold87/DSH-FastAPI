from fastapi import FastAPI
from router.router import driver

app = FastAPI()

app.include_router(driver)