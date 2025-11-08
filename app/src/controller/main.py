from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from model import db_manager
from controller import routers

db_manager.Base.metadata.create_all(bind=db_manager.engine)

# the app
app = FastAPI()


# static routes
app.mount("/static", StaticFiles(directory="view/static"), name="static")


# dynamic APIrouters

app.include_router(routers.userCrudRouter, prefix="/api/json")
app.include_router(routers.templateRouter, prefix="/api/html")

