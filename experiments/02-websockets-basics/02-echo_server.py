import asyncio
from websockets.asyncio.server import serve

async def handle(websocket):
    async for message in websocket:
        print(f"Received message: {message}")
        await websocket.send(f"Echo: {message}")

async def main():
    async with serve(handle, "localhost", 8765)as server:
        print("Server started on ws://localhost:8765")
        await server.serve_forever()

asyncio.run(main())
