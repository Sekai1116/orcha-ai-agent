import os
import httpx

async def fetch_weather(city: str):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        # Fallback mock response
        return {
            "tool": "WeatherTool",
            "parameters": {"city": city},
            "result": "22°C and sunny (mocked)"
        }

    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        async with httpx.AsyncClient() as client:
            res = await client.get(url)
            data = res.json()
            temp = data['main']['temp']
            condition = data['weather'][0]['description']
            return {
                "tool": "WeatherTool",
                "parameters": {"city": city},
                "result": f"{temp}°C and {condition}"
            }
    except Exception:
        # Fallback if request fails
        return {
            "tool": "WeatherTool",
            "parameters": {"city": city},
            "result": "22°C and sunny (mocked fallback)"
        }
