class effects:
  def __init__(self, name, description, level,ability =[],oname=[]):
    self.name = name
    self.description = description
    self.level = level
    self.ability = ability #This will describe things such as damage over time, mana loss etc
    self.oname = oname #for general name tracking purposes will be used so that skills can be updated
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
    ab =[]
    if input("would you like to add and ability (y/n)") in ["yes", "YES", "Yes","y", "Y"]: 
      aflag = 0
      print("Mp is for Manapool, Hp for healthpool, Mpf is for MP over time and Hpf as the same, the number will denote the strength of which ie Mp -100 0 is -100 from mana pool while Hpf -10 2 is -10 health per unit of time for 2 ticks max:  ")#kinda confusing but game mechanics are complex also allow for other attacks over time ie damage soul and whatever #
      while aflag == 0:
        ability = input("What effect would you like?: ")
        if ability in ["yes", "YES", "Yes","y", "Y"]:
          aflag = 1
          continue
        ab.append(ability)
    etemp = effects(name,description,lvlcap,ab)
    db.append(etemp)
    off = 1
    #print(db)
  with open('effects_db.pkl','wb') as pickle_file:
    for x in db:
      pickle.dump(x,pickle_file)
  return namedb

def e_mod():
  import pickle
  db = []
  with open('effects_db.pkl','rb') as pickle_file:
    try:
      while 1:
        db.append(pickle.load(pickle_file))
    except EOFError:
      pass
  print("The current Effects are: ")
  for x in db:
    print(vars(x))
    print("\n")
  while 1:
    name = input("which would you like to change? ")
    Tflag = 0
    for x in db:
      if x.name == name:
        Tflag = 1
        if input("would you like to change the name (y/n)") in ["yes", "YES", "Yes","y", "Y"]: 
          x.name = input("What is the new name?: ")
          x.oname = name
        if input("would you like to change the description (y/n)") in ["yes", "YES", "Yes","y", "Y"]: 
          x.description = input("What is the new Description?: ")
        if input("would you like to change the abilities (y/n)") in ["yes", "YES", "Yes","y", "Y"]: 
          aflag = 0
          ab =[]
          print("Mp is for Manapool, Hp for healthpool, Mpf is for MP over time and Hpf as the same, the number will denote the strength of which ie Mp -100 0 is -100 from mana pool while Hpf -10 2 is -10 health per unit of time for 2 ticks max:  ")#kinda confusing but game mechanics are complex also allow for other attacks over time ie damage soul and whatever #
          while aflag == 0:
            ability = input("What effect would you like?: ")
            if ability in ["yes", "YES", "Yes","y", "Y"]:
              aflag = 1
              continue
            ab.append(ability)
          x.ability = ab
    if Tflag == 0:
      print("That was not a valid effect: ")
      continue    
    if input("would you like to continue") not in ["yes", "YES", "Yes","y", "Y"]:
      break
  with open("effects_db.pkl","wb") as pickle_file:
    for x in db:
      pickle.dump(x,pickle_file)
  return

