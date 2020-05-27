class effects:
  def __init__(self, name, description, level,ability =[]):
    self.name = name
    self.description = description
    self.level = level
    self.ability = ability #This will describe things such as damage over time, mana loss etc
    return 
  def lvl_up(self):
    self.level = self.level + 1
  def ability_add(self):
    db = []
    while 1:
      db.append(input("What ability does this effect have? "))
      break
def effect_make():
  import pickle
  off = 0
  flag = 0
  db = []
  namedb= []
  with open('effects_db.pkl','rb') as pickle_file:
    try:
      while 1:
        db.append(pickle.load(pickle_file))
    except EOFError:
      pass
  while off ==0:
    name = input('What is the name of this effect?: ')
   # print (name)
    if name == "stop" or name == "STOP" or name == "Stop":
      print("Here are the current effects")
      for x in db:
        print (x.name)
      return 0 #in order to note that the effect needs to be added from the current list of valid effects
    for x in db:
      if x.name == name:
        flag = 1
        break
    if flag == 1:
      print("That effects already exists: ")
      flag = 0
      continue
    #print("1")
    namedb.append(name)
    description = input("What should its description?: ")
    lvlcap = int(input("What is the maximum level for this effect?: "))
    etemp = effects(name,description,lvlcap)
    db.append(etemp)
    off = 1
    #print(db)
  with open('effects_db.pkl','wb') as pickle_file:
    for x in db:
      pickle.dump(x,pickle_file)
  return namedb