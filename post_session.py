from app.database import supabase
from datetime import datetime

async def generate_summary(session_id):
    events = supabase.table("events") \
        .select("content") \
        .eq("session_id", session_id) \
        .execute()

    conversation = " ".join([e["content"] for e in events.data])

    summary = conversation[:200] + "..."  # simple mock summary

    supabase.table("sessions").update({
        "summary": summary,
        "duration": len(conversation)
    }).eq("id", session_id).execute()
