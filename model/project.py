

class Project:

    def __init__(self, id=None, name=None, description=None):
        self.id = id
        self.name = name
        self.description = description

    def __repr__(self):
        return "%s: %s" % (self.id, self.name)

    def __eq__(self, other):
        return (self.id == other.id or self.id is None or other.id is None) and self.name == other.name
        # return (self.name == other.name or self.name is None or other.name is None) and self.id == other.id
        # and self.description == other.description