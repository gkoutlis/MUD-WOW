import asyncio
from websockets.asyncio.server import serve

async def handler(websocket):
    async for message in websocket:
        await websocket.send(f"You said {message}")

async def main():
    async with serve(handler, "localhost", 8765) as server:
        print("Server listening on ws://localhost:8765")
        await server.serve_forever()

asyncio.run(main())