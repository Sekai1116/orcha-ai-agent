from services.worldtime import fetch_time

async def get_local_time(city: str):
    return await fetch_time(city)