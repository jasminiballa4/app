import asyncio

async def stream_llm_response(user_message: str):
    response = f"AI response to: {user_message}"
    tokens = response.split(" ")

    for token in tokens:
        await asyncio.sleep(0.2)  # simulate streaming
        yield token + " "
