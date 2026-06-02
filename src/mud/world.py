from mud import Room

rooms = {
    "tavern": Room(
        name="Tavern",
        description="A cozy tavern with a warm fire crackling in the corner.",
        exits={"north":"cave", "east":"forest","south":"desert", "west":"abyss"},
    ),
    "cave": Room(
        name="Cave",
        description="A dark cave full of mysteries and threats.",
        exits={"south":"tavern"}
    ),
    "desert": Room(
        name="Desert",
        description="A rocky desert with no fire no hope full of experience.",
        exits={"north":"tavern"}
    ),
    "forest": Room(
        name="Forest",
        description="Full of waterfalls, elves and secrets.",
        exits={"west":"tavern"}
    ),
    "abyss": Room(
        name="Abyss",
        description="Dark magic conquers the strings of anti-life.",
        exits={"east":"tavern"}
    ),
}

players = {}
