from fastapi import FastAPI
from fastapi.params import Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class Detail(BaseModel):
    bmi: int
    sleep_duration: int
    smoking_index: int
    drinking_index: str


depression_detail = [{
    "bmi": 20,
    "sleep_duration": 12,
    "smoking_index": 40,
    "drinking_index": "Never"
}]


@app.get("/")
def root():
    return {"message": "Welcome to depression detection API"}


@app.post("/detail")
def send_detail(detail: Detail):
    depression_detail.append(detail.dict())
    print(depression_detail[1])
    return {"Data": "New Post Created Succesfully."}


@app.get("/detail")
def get_detail():
    latest = len(depression_detail)
    return {"data": depression_detail[latest - 1]}
