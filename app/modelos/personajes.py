class Personaje:
    def __init__(self, id, name, status, species, type, gender, image):
        self.id = id
        self.name = name
        self.status = status
        self.species = species
        self.type = type
        self.gender = gender
        self.image = image

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status,
            'species': self.species,
            'type': self.type,
            'gender': self.gender,
            'image': self.image
        }
