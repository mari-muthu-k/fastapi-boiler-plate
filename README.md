# fastapi-boiler-plate
## Setup : 
1. Setup this repo locally
2. `pip -r requirements.txt`
3. Edit database connection details in `config.json`

## Run project :
1. If you're using linux , run `sudo chmod +x ./app.sh` and `./app.sh`
2. If you're using windows , run `uvicorn main:app --reload`

## To view all the available endpoints :
- set `listAPI` to true in `config.json`
- start the application
- search `host:port/docs` [ example : http://127.0.0.1:8000/docs ]

## To send email :
- configure email connection in `config.json`
- start to use `controller/email:sendEmail` function
