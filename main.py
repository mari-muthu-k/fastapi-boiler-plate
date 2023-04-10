from env import appConfig as config
from fastapi import FastAPI,Request,Response,Depends
from fastapi.responses import JSONResponse


from db import engine,Base

from fastapi.middleware.cors import CORSMiddleware
from starlette_session import SessionMiddleware


from router import example
from exception import customException

app = FastAPI() if config.LIST_ENDPOINTS else FastAPI(openapi_url="")

#Create DB schema
Base.metadata.create_all(bind=engine)

#Session config
app.add_middleware(
    SessionMiddleware,
    secret_key = config.COOKIE_SECRET_KEY,
    cookie_name = config.COOKIE_NAME,
    max_age = config.COOKIE_MAX_AGE,
    same_site = config.COOKIE_SAME_SITE,
    domain = config.COOKIE_DOMAIN
    )

#CORS config
app.add_middleware( 
    CORSMiddleware, 
    allow_origins=config.AUTH_DOMAINS, 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"]
    )

app.include_router(example.router,prefix="/api")
@app.get("/")
def root():
    return 'Start building amazing applications !'

@app.exception_handler(customException)
async def exception_handler(request: Request, exc: customException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message":exc.message},
    )