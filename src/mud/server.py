import asyncio
from mud.player import Player
from mud.world import players
from websockets.asyncio.server import serve





async def broadcast(message):
    for ws in players:
        try:
            await ws.send(message)
        except Exception:
            pass

async def handler(websocket):
    await websocket.send("Whats your name?")
    name = await websocket.recv()
    player = Player(websocket, name)
    players[websocket] = player
    print(f"{player.name} joined the chat!")
    await broadcast(f"{player.name} joined the chat!")

    try:
        async for message in websocket:
            if message.startswith("/who"):
                names = [p.name for p in players.values()]
                names_str = ", ".join(names)
                await websocket.send(f"Online players: {names_str} ")
            elif message.startswith("/help"):
                commands = "/help, /who, /nick"
                await websocket.send(commands)
            elif message.startswith("/nick"):
                parts = message.split(" ", 1)
                if len(parts) < 2:
                    await websocket.send(f"You must enter a name!")
                    continue
                new_name = parts[1]
                await broadcast(f"{player.name} is now known as {new_name}")
                player.name = new_name


            elif message.startswith("/"):
                await websocket.send("Unknown command")

            else:
                print(f"Received from {player.name}: {message}")
                await broadcast(f"{player.name}: {message}")
    finally:
        players.pop(websocket,None)
        print(f"Player {player.name} left the chat!")
        await broadcast(f"{player.name} left the chat!")

async def  main():
    async with serve(handler, "localhost", 8765) as server:
        print("Chat server started on ws://localhost:8765")
        await server.serve_forever()

asyncio.run(main())
