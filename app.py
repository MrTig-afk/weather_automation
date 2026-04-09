import os
from dotenv import load_dotenv
load_dotenv()
import requests
from supabase import create_client
from datetime import datetime

cities = ["Paris", "London", "Tokyo", "New York"]

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
WEATHER_API = os.getenv("WEATHER_API")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

for city in cities:
    r = requests.get(f'http://api.weatherapi.com/v1/current.json?key={WEATHER_API}&q={city}')
    data = r.json()
    
    record = {
        "city": data["location"]["name"],
        "temperature": data["current"]["temp_c"],
        "humidity": data["current"]["humidity"],
        "timestamp": data["location"]["localtime"],
        "ingested_at": datetime.now().isoformat()
    }
    
    supabase.table("weather_readings").insert(record).execute()
    print(f"Inserted {city}")

print("Done!")