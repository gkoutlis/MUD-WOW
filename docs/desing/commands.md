## Movement

- `look` — describe the current room (exits, items, monsters, players present)
- `go <direction>` — move to an adjacent room (north / south / east / west / up / down)
- `dash <direction>` — special move covering two rooms in one action (limited use, cooldown)

## Combat

- `attack <target>` — attack a monster or player
- `switch <target>` — change current target (useful when multiple enemies are in the room, e.g. two orcs in a cave)
- `defend` — raise shield to reduce incoming damage this turn
- `heal <target>` — heal yourself or an ally
- `run` — flee from combat (fails if target is more than 1 level above yours)
- `use heal potion` — restore HP
- `use strength potion` — temporary strength boost
- `use revive potion` — bring a fallen ally back to life

## Social

- `say <message>` — speak to players in the same room
- `whisper <player> <message>` — send a private message to one player
- `ping` — signal "I'm ready" to the group
- `/who` — list online players
- `/status <afk|ready>` — set your combat availability
- `/inspect <player>` — view another player's stats
- `/stats` — view your own stats (HP, mana, level, equipment)

## Inventory

- `inventory` — show what you're carrying
- `equip <item>` — equip a weapon or armor piece
- `unequip <item>` — remove an equipped item
- `drop <item>` — drop an item in the current room
- `destroy <item>` — permanently destroy an item
- `transfer <item> to <player>` — give an item to another player in the same room

## Loot

- `pick up <item>` — pick up an item from the ground
- `loot <target>` — take items from a defeated enemy

## System

- `/help` — show available commands
- `/quit` — save and end your session (only available in safe zones like taverns)