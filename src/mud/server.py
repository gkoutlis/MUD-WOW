import asyncio
from mud.player import Player
from mud.world import players, rooms
from mud.broadcasting import broadcast, broadcast_to_room
from mud.commands.chat import help_command, who_command, nick_command
from mud.commands.world import look_command, go_command
from websockets.asyncio.server import serve


COMMANDS = {
    "/help": help_command,
    "/who": who_command,
    "/nick": nick_command,
    "look": look_command,
    "go": go_command,
}


async def handler(websocket):
    await websocket.send("Whats your name?")
    name = await websocket.recv()
    player = Player(websocket, name)
    players[websocket] = player
    print(f"{player.name} joined the chat!")
    await broadcast(f"{player.name} joined the chat!")

    try:
        async for message in websocket:
            parts = message.split(" ", 1)
            first_word = parts[0]
            args = parts[1] if len(parts) > 1 else ""

            if first_word in COMMANDS:
                await COMMANDS[first_word](player, args, websocket)
            elif message.startswith("/"):
                await websocket.send("Unknown command")
            else:
                print(f"Received from {player.name}: {message}")
                await broadcast(f"{player.name}: {message}")
    finally:
        players.pop(websocket, None)
        print(f"Player {player.name} left the chat!")
        await broadcast(f"{player.name} left the chat!")


async def main():
    async with serve(handler, "localhost", 8765) as server:
        print("Chat server started on ws://localhost:8765")
        await server.serve_forever()


asyncio.run(main())