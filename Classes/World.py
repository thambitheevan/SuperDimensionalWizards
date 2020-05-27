#This File will describe the structure of the world
class plane:
  def __int__(self,name,regions,strength,stability, aplanes ):
    self.name = name
    self.regions = regions #List of regions contained
    self.strength = strength #The 'power' of the plane
    self.stability = stability #How stable the plane is
    self.aplanes = aplanes #
    return
  
class region:
  def __init__(self,name,manalevel,rcord=(0,0), aregions=[],biome='Default',locations=[]):
    self.name = name 
    self.manalevel = manalevel #The energy level that exists ie 0 with no mana 10 with a high primal mana flow and -10 sucking mana away
    self.rcoord = rcord # The 2d location of it
    self.aregion = aregions #THe list of regions attached to this one
    self.biome = biome
    self.locations = locations
    return

class location:
  def __init__(self, name,description, effects=[],creatures=[],lcord=(0,0)):
    self.name = name
    self.description = description
    self.effects = effects #List of all the effects that are present in this location
    self.creatures = creatures #All of the creatures that may spawn here
    self.lcord = lcord #The tuple holding the coords of location in the regions
    return
