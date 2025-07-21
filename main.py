from fastapi import FastAPI
from models.schemas import CityRequest
from tools.planner import plan_my_city_visit
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

@app.post("/plan_visit")
async def plan_visit(req: CityRequest):
    return await plan_my_city_visit(req.city)