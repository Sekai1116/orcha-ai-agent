import asyncio
from tools.weather import get_weather
from tools.time import get_local_time
from tools.city_facts import get_city_facts

async def plan_my_city_visit(city: str):
    thinking = f"To help you plan your visit to {city}, I'll first get some facts, then fetch the current weather and time."

    city_facts, weather, time = await asyncio.gather(
        get_city_facts(city),
        get_weather(city),
        get_local_time(city)
    )

    response = f"{city_facts['result']} It's currently {weather['result']}. The local time is {time['result']}."

    return {
        "thinking": thinking,
        "function_calls": [
            {"tool": city_facts['tool'], "parameters": city_facts['parameters']},
            {"tool": weather['tool'], "parameters": weather['parameters']},
            {"tool": time['tool'], "parameters": time['parameters']},
        ],
        "response": response
    }