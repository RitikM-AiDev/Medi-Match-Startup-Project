from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from msg_agent import forward_msg_generator
from a_sugession import hospital_analysis

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


class ForwardMsgModel(BaseModel):
    title: str
    description: str


@app.post("/frwdMsg")
def forward_msg(data: ForwardMsgModel):
    summary = forward_msg_generator(
        data.title,
        data.description
    )
    hospitals = [
    {
        "name": "Meenakshi Mission Hospital",
        "address": "Lake Area, Melur Road, Madurai",
        "rating": 4.6,
        "reviews": 8500,
        "distance_km": 5.2,
        "specialties": ["Cardiology", "Neurology", "Oncology"],
        "emergency": True,
        "icu": True,
        "beds_available": 35
    },
    {
        "name": "Apollo Speciality Hospital",
        "address": "Madurai, Tamil Nadu",
        "rating": 4.5,
        "reviews": 6200,
        "distance_km": 7.8,
        "specialties": ["Cardiology", "Orthopedics"],
        "emergency": True,
        "icu": True,
        "beds_available": 22
    },
    {
        "name": "Velammal Medical College Hospital",
        "address": "Madurai, Tamil Nadu",
        "rating": 4.3,
        "reviews": 3200,
        "distance_km": 10.1,
        "specialties": ["General Medicine", "Cardiology"],
        "emergency": True,
        "icu": True,
        "beds_available": 18
    },
    {
        "name": "Government Rajaji Hospital",
        "address": "Madurai, Tamil Nadu",
        "rating": 4.1,
        "reviews": 5000,
        "distance_km": 6.5,
        "specialties": ["Trauma Care", "Emergency Medicine"],
        "emergency": True,
        "icu": True,
        "beds_available": 50
    },
    {
        "name": "Devadoss Multispeciality Hospital",
        "address": "Madurai, Tamil Nadu",
        "rating": 4.4,
        "reviews": 2800,
        "distance_km": 4.3,
        "specialties": ["Cardiology", "Neurology"],
        "emergency": True,
        "icu": True,
        "beds_available": 12
    }
]
    result = hospital_analysis(summary,hospitals)
    print(result)
    return {
        "message": summary
    }
    
    
