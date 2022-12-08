class Capitulo:
    def __init__(self, id, name, type, dimension,foto):
        self.id = id
        self.name = name
        self.type = type
        self.dimension = dimension
        self.foto = foto

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'dimension': self.dimension,
            'foto':self.foto

        }
