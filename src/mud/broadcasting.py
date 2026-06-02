from mud.world import players


async def broadcast(message):
    for ws in players:
        try:
            await ws.send(message)
        except Exception:
            pass

async def broadcast_to_room(room_name, message, exclude=None):
    for ws, player in players.items():
        if player.room == room_name and ws != exclude:
            try:
                await ws.send(message)
            except Exception:
                pass