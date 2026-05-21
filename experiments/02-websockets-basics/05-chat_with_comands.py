import asyncio
from websockets.asyncio.server import serve

players = {}

async def broadcast(message):
    for ws in players:
        try:
            await ws.send(message)
        except Exception:
            pass

async def handler(websocket):
    await websocket.send("Whats your name?")
    name = await websocket.recv()
    players[websocket] = name
    print(f"{name} joined the chat!")
    await broadcast(f"{name} joined the chat!")

    try:
        async for message in websocket:
            if message.startswith("/who"):

                names = ", ".join(players.values())
                await websocket.send(f"Online players: {names} ")
            elif message.startswith("/"):
                await websocket.send("Unknown command")

            else:
                print(f"Received from {name}: {message}")
                await broadcast(f"{name}: {message}")
    finally:
        players.pop(websocket,None)
        print(f"Player {name} left the chat!")
        await broadcast(f"{name} left the chat!")

async def  main():
    async with serve(handler, "localhost", 8765) as server:
        print("Chat server started on ws://localhost:8765")
        await server.serve_forever()

asyncio.run(main())
