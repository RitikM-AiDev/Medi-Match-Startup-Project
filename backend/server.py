from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:5173",
    "https://yourdomain.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,     
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class forward_msg_model(BaseModel):
    title : str
    description : str 

def forward_msg(data : forward_msg_model):
    print(data.title)
    print(data.description)
