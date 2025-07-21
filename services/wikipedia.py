import httpx

async def fetch_city_facts(city: str):
    try:
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{city}"
        async with httpx.AsyncClient() as client:
            res = await client.get(url)
            data = res.json()
            extract = data.get("extract", f"No info found for {city}.")
            return {
                "tool": "CityFactsTool",
                "parameters": {"city": city},
                "result": extract
            }
    except Exception:
        return {
            "tool": "CityFactsTool",
            "parameters": {"city": city},
            "result": f"{city} is a remarkable place (mocked fallback)."
        }