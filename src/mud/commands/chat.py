from mud.world import players
from mud.broadcasting import broadcast


async def help_command(player, args, websocket):
    commands = "/help, /who, /nick, look, go"
    await websocket.send(commands)


async def who_command(player, args, websocket):
    names = [p.name for p in players.values()]
    names_str = ", ".join(names)
    await websocket.send(f"Online players: {names_str}")


async def nick_command(player, args, websocket):
    new_name = args.strip()
    if not new_name:
        await websocket.send("You must enter a name!")
        return
    await broadcast(f"{player.name} is now known as {new_name}")
    player.name = new_name