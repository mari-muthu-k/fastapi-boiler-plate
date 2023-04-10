from fastapi import APIRouter,Request,Response,Depends,Path
from controller.http import HTTP_RESPONSE


router = APIRouter()

@router.get("/example")
async def login(req:Request,res:Response):
    return HTTP_RESPONSE(statusCode=200).returnMessage(res)

@router.get("/badrequest")
async def login(req:Request,res:Response):
    return HTTP_RESPONSE(statusCode=400).returnCustomMessage(res,"Bad request !")