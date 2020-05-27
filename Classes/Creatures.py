#Will describe the Creatures in the game
class creature:
    def __init__(self, name, level, cast, manapool,manaprops, body, knowledge, bloodline,
                 skills):
        self.name = name
        self.level = level
        self.cast = cast
        self.manapool = manapool
        self.manaprops=manaprops
        self.body = body
        self.knowledge = knowledge
        self.bloodline = bloodline
        self.skills = skills
