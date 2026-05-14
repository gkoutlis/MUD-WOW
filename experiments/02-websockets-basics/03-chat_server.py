import asyncio
from websockets.asyncio.server import serve

connected_players = set()

async def broadcast(message):
    for player in connected_players:
        try:
            await player.send(message)
        except Exception as e:
            pass

async def handler(websocket):
    connected_players.add(websocket)
    print(f"New client connected: {websocket}")
    try:
        async for message in websocket:
            print(f"Received from {websocket.id}: {message}")
            await broadcast(message)

    finally:
        connected_players.discard(websocket)
        print(f"Client disconnected: {websocket}")

async def main():
    async with serve(handler, "localhost", 8765) as server:
        print("Chat server started on ws://localhost:8765")
        await server.serve_forever()



asyncio.run(main())