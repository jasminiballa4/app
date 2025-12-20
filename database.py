from supabase import create_client
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

async def create_session(session_id):
    supabase.table("sessions").insert({
        "id": session_id,
        "start_time": datetime.utcnow()
    }).execute()

async def save_event(session_id, event_type, content):
    supabase.table("events").insert({
        "id": str(os.urandom(16).hex()),
        "session_id": session_id,
        "event_type": event_type,
        "content": content
    }).execute()

async def close_session(session_id):
    supabase.table("sessions").update({
        "end_time": datetime.utcnow()
    }).eq("id", session_id).execute()
