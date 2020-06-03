#Skills Are the main way that combat actions can be taken in as 
#They can Target Health, Mana Pool or can apply other effects aswell
# SKills work via activating effects 
#Cantrips and Spells are examples of Skills
#Skills can also be inherited from creatures or plants

class Skills:
  def __init__(self, name, cat, effects):
    self.name = name
    self.cat = cat #This is the set of Cantrips, Physical Attacks and Spells
    self.effects = effects
    return
class creature:
  def __init__(self,name,Mp,Hp,skills,rare,drops = []):
    self.name = name
    self.Mp = Mp
    self.Hp = Hp
    self.skills = skills
    self.rare = rare
    self.drops = drops #Will be updated when materials are added from the materials section
    return
class plant:
  def __init__(self,name,description,skills=[],drops=[]):
    self.name = name
    self.description = description
    self.skills = skills
    self.drops = drops
    return

class effects: #For General use Purposes
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
  def ability_translate(self): #This function provides returns the list of abilities in terms of usable data:
    db = []
    damlist = [0,0,0,0]#MP,HP,Mpf,Hpf this is also the returned value
    for x in self.ability:
      for i in range(0,len(x)):
        if x[i] == " " or x[i] == ' ':
          db.append(i)
      alpha = x[:db[0]]
      beta = x[db[0]+1:db[1]]
      kappa = x[db[1]+1:]
    rval = -1
    if alpha in ["mp","Mp","MP"]:
      rval = 0
    if alpha in ["hp","Hp","HP"]:
      rval = 1
    if alpha in ["mpf","Mpf","MPf","MPF"]:
      rval = 2
    if alpha in ["hpf","Hpf","HPf","HPF"]:
      rval = 3
    if rval in [0,1]:
      damlist[rval] = beta
    if rval in [2,3]:
      damlist[rval] = [beta,kappa]
    if rval == -1:
      return -1
    return damlist

def S_make():#Honestly dont use this
  import pickle
  db=[]
  effectdb=[]
  with open('skills_db.pkl','rb') as pickle_file:
    try:
      while 1:
        db.append(pickle.load(pickle_file))
    except EOFError:
      pass
  with open('effects_db.pkl','rb') as pickle_file:
    try:
      while 1:
        effectdb.append(pickle.load(pickle_file))
    except EOFError:
      pass
  flag = 1
  while flag==1:
    name = input("What is the name of this skill?: ")
    for x in db:
      if name == x.name:
        print("That Skill Already Exists:")
        flag = 0
    if flag ==1:
      break
    flag =1
  cat = input("what is the catagory of this skill: ") #p for physical attack, c for cantrip, s for spell
  print("All of the current effects are:")
  for x in effectdb:
    print(x.name)
  print("add effects as you desire: ")
  effect =[]
  while 1:
    Teffect = input("What is the effect called: ")
    if Teffect == "stop" or Teffect == "Stop" or Teffect == "STOP":
      break
    effect.append(Teffect)
  db.append(Skills(name,cat,effect))
  with open("skills_db.pkl","wb") as pickle_file:
    for x in db:
      pickle.dump(x,pickle_file)  
  return

def s_read():
  import pickle
 #This function will print out the list of all creatures that exist in our data base
  with open('skills_db.pkl','rb') as pickle_file:
    print("The Currently Locked Set of Skills are: ")
    try:
      while 1:
        print(vars(pickle.load(pickle_file)))
    except EOFError:
      pass
  return
  
def s_update():
  #This function reads from the creature/plant db and adds the skills to the skills database
  import pickle
  db=[]
  cdb=[]
  pdb = []
  effectdb = []
  with open('skills_db.pkl','rb') as pickle_file:
    try:
      while 1:
        db.append(pickle.load(pickle_file))
    except EOFError:
      pass
  with open('creature_db.pkl','rb') as pickle_file:
    try:
      while 1:
        cdb.append(pickle.load(pickle_file))
    except EOFError:
      pass
  with open('plant_db.pkl','rb') as pickle_file:
    try:
      while 1:
        pdb.append(pickle.load(pickle_file))
    except EOFError:
      pass
  with open('effects_db.pkl','rb') as pickle_file:
    try:
      while 1:
        effectdb.append(pickle.load(pickle_file))
    except EOFError:
      pass
  for x in cdb:
    #goes across all the creatures
    for y in x.skills:
      #goes across all skills in that creature
      sflag = 0
      for z in db:
        if z.name == y:
          sflag = 1
          continue
        if sflag == 1:
          break
      if sflag == 0:
        print(y)
        cat = input("What is the catagory of this skill?: ")
        print("All of the current effects are:")
        for x in effectdb:
          print(x.name)
        print("type add for new effects")
        effect =[]     
        while 1:
          Teffect = input("What is the effect called: ")
          if Teffect in ['add','ad','Add',"ADD"]:
            effect_make()
            print("type in the effect again to add it")
            continue
          if Teffect == "stop" or Teffect == "Stop" or Teffect == "STOP":
            break
          effect.append(Teffect)
        db.append(Skills(y,cat,effect))
  for x in pdb:
    #goes across all the plants
    for y in x.skills:
      #goes across all skills in that plant
      sflag = 0
      for z in db:
        if z.name == y:
          sflag = 1
          continue
        if sflag == 1:
          break
      if sflag == 0:
        print(y)
        cat = input("What is the catagory of this skill?: ")
        print("All of the current effects are:")
        for x in effectdb:
          print(x.name)
        print("type add to make a new effect ")
        effect =[]     
        while 1:
          Teffect = input("What is the effect called: ")
          if Teffect in ['add','ad','Add',"ADD"]:
            effect_make()
            print("type in the effect again to add it")
            continue
          if Teffect == "stop" or Teffect == "Stop" or Teffect == "STOP":
            break
          effect.append(Teffect)
        db.append(Skills(y,cat,effect))
  with open("skills_db.pkl",'wb') as pickle_file:
    for x in db:
      pickle.dump(x,pickle_file)
  return
        
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




  

