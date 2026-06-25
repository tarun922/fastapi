from fastapi import FastAPI
from data import Data
from rag import Model
app = FastAPI()


db=Data()
req=Model()

@app.get("/")
def home():
    return "home screen runnings"

@app.get("/create")

def create_user(name:str):
    m=Data().set_user(str(name))
    return m
@app.get("/ask")

def ask(key:str,q:str):

    u=Data().get_user(key)
    try :

        user=u["user"]

    except:
        return {"error":"wrong key "}

    responce=req.get_req(q)
    Data().update_credits(user,sub=1)
    return responce
@app.get("/check")

def check(name:str):
    try :
        s=Data().get_credit(name)
        return s
    except:
        return {"error":"wrong user "}



