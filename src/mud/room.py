

class Room:
    def __init__(self, name, description, exits = None):
        self.name = name
        self.description = description
        self.exits = exits if exits is not None else {}