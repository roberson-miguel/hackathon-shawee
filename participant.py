class Participant:
    def __init__(self, name, role, level):
        self.name = name
        self.role = role
        self.level = level

    def info(self):
        print("Name: " + self.name + " Role: " + int(self.role) + " Level: " + int(self.level))

