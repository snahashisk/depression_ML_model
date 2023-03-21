from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


class Detail(BaseModel):
    bmi: int
    sleep_duration: int
    smoking_index: int
    drinking_index: str


@app.get("/")
def root():
    return {"message": "Welcome to depression detection API"}


# @app.post("/detail")
# def storeDetail(detail: Detail):
#     detail_dict = detail.dict()
#     return {"Data": "Data recieved"}


@app.post("/detail")
def createPost(new_post: Detail):
    print(new_post.bmi)
    return {"Data": "New Post Created Succesfully."}
