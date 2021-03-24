from fastapi import FastAPI
from fastapi.responses import JSONResponse
# from src.server.utils import get_credentials
# import psycopg2
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)

app = FastAPI()
# user, db, password, host, port = get_credentials()
# con = psycopg2.connect(database=db, user=user,
#                        password=password, host=host, port=port)
# cur = con.cursor()


@app.get("/")
def read_root():
    return 'server is running'


@app.get("/start")
async def connect2db():
    user, db, password, host, port = get_credentials()
    con = psycopg2.connect(database=db, user=user,
                           password=password, host=host, port=port)
    con.close()
    logging.info("Database opened successfully")
    return JSONResponse(
        status_code=200,
        content={
            'info': 'Database opened successfully'
        }
    )