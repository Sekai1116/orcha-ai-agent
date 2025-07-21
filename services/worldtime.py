import os
import httpx
from datetime import datetime

async def fetch_time(city: str):
    tzdb_key = os.getenv("TIMEZONEDB_API_KEY")
    ow_key = os.getenv("OPENWEATHER_API_KEY")

    if not (tzdb_key and ow_key):
        return {
            "tool": "TimeTool",
            "parameters": {"city": city},
            "result": "3:00 PM (fallback - missing API keys)"
        }

    try:
        async with httpx.AsyncClient() as client:
            # Step 1: Get coordinates from OpenWeatherMap
            geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={ow_key}"
            geo_res = await client.get(geo_url)
            geo_data = geo_res.json()
            if not geo_data:
                raise ValueError("Invalid city name")

            lat = geo_data[0]["lat"]
            lon = geo_data[0]["lon"]

            # Step 2: Get time from TimeZoneDB
            tz_url = f"http://api.timezonedb.com/v2.1/get-time-zone?key={tzdb_key}&format=json&by=position&lat={lat}&lng={lon}"
            tz_res = await client.get(tz_url)
            tz_data = tz_res.json()
            if tz_data["status"] != "OK":
                raise ValueError("Failed to fetch time")

            time_str = tz_data["formatted"]  # e.g. 2025-07-21 19:16:57
            dt_obj = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
            formatted = dt_obj.strftime("%I:%M %p").lstrip("0")

            return {
                "tool": "TimeTool",
                "parameters": {"city": city},
                "result": formatted
            }

    except Exception:
        return {
            "tool": "TimeTool",
            "parameters": {"city": city},
            "result": "3:00 PM (fallback)"
        }
