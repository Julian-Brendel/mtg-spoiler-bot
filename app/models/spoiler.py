from .base import Base


class Spoiler(Base):

    # Sets
    sets = []

    # Get sets from source
    def __init__(self):
        Base.__init__(self)

    # Set sets
    def set_sets(self, sets):
        self.sets = sets

    # Append set
    def append_set(self, set):
        self.sets.append(set)

    # Get sets
    def get_sets(self):
        return self.sets

    # Get sets length
    def get_sets_length(self):
        return len(self.sets)

    # Get the latest set
    def get_first_set(self):
        return self.sets[0]

    # Find set
    def find_set(self, set_name):
        for set in self.sets:
            if set.get_name() == set_name:
                return set

        return False

    # Get all new cards
    def get_new_cards(self):
        cards = []

        for set in self.sets:
            cards += set.get_new_cards()

        return cards






