from services.wikipedia import fetch_city_facts

async def get_city_facts(city: str):
    return await fetch_city_facts(city)