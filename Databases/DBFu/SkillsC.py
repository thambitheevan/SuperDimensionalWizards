#Skills Are the main way that combat actions can be taken in as 
#They can Target Health, Mana Pool or can apply other effects aswell
# SKills work via activating effects 
#Cantrips and Spells are examples of Skills
#Skills can also be inherited from bloodlines or creatures

class Skills:
  def __init__(self, name, cat, effects):
    self.name = name
    self.cat = cat #This is the set of Cantrips, Physical Attacks and Spells
    self.effects = effects
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
  





  

