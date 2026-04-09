import os
from dotenv import load_dotenv
load_dotenv() 
from fastapi import FastAPI
from supabase import create_client

SUPABASE_URL = os.getenv("SUPABASE_URL")  # GOOD
SUPABASE_KEY = os.getenv("SUPABASE_KEY")  # GOOD

app= FastAPI()

@app.get("/")
def root():
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    result = supabase.table("weather_readings").select("*").limit(10).execute()
    return result.data
    