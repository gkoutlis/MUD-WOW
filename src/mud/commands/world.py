from mud.world import players, rooms
from mud.broadcasting import broadcast_to_room


def describe_room(player):
    room = rooms[player.room]
    exits_str = ", ".join(room.exits.keys())
    players_here = [p.name for p in players.values() if p.room == player.room]
    players_str = ", ".join(players_here)
    return (
        f"== {room.name} ==\n"
        f"{room.description}\n"
        f"Exits: {exits_str}\n"
        f"Players here: {players_str}"
    )


async def look_command(player, args, websocket):
    output = describe_room(player)
    await websocket.send(output)


async def go_command(player, args, websocket):
    direction = args.strip()
    if not direction:
        await websocket.send("You must enter a direction!")
        return

    current_room = rooms[player.room]
    if direction not in current_room.exits:
        await websocket.send("You can't go that way!")
        return

    destination = current_room.exits[direction]
    await broadcast_to_room(
        player.room,
        f"{player.name} left for {direction}",
        exclude=websocket,
    )
    player.room = destination
    await broadcast_to_room(player.room, f"{player.name} arrived")
    await websocket.send(describe_room(player))