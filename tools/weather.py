from services.openweather import fetch_weather

async def get_weather(city: str):
    return await fetch_weather(city)