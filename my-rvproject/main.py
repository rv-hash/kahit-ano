from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "101"}
@app.get("/imgay")
def ilalagaynanyosir(id=int,name=str):
    return {"my id is: ": id, "my name is:":name}
    


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str ):
    return {"item_id": item_id, "q": q}

@app.get("/calculator")
def read_item(first_Num: int, Second_num: int ):
    result = first_Num + Second_num
    return {"the result is :":result }