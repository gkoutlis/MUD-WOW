

class Player:
    def __init__(self,websocket, name, room = "tavern"):
        self.websocket = websocket
        self.name = name
        self.room = room