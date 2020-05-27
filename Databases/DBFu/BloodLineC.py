#This will read from the set of all monsters and be used to create bloodline Automatically from them the user will input the bloodline special effects

class bloodline:
  def __init__(self, name, maxpowerlevel, skills, reqknowledge, success=0 ,value = 0,status=0):
    self.name = name
    self.maxpowerlevel = maxpowerlevel
    self.skills = skills #comes from the creatures skills
    self.reqknowledge = reqknowledge #3 prereq + better chance and usage 
    self.value = value
    self.success = success #Chance of successful fusing
    self.value = value #Value of the bloodline
    self.status = status #Ability to transform into the creature 1->100 ie at 50 can transform fully but not use all of its abilities
    return
  

  

