import os
from fastapi import  APIRouter


base_router =  APIRouter()

@base_router.get("/")
def welcome_msg():
    app_name = os.environ["APP_NAME"]
    return {
        "message" : app_name
    }