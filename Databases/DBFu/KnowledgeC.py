#The Database of the potential Knowledge Groups
class effects:#Coming from the effects class folder just easier to put here aswell
  def __init__(self, name, description, lvlcap,level=0,ability =[]):
    self.name = name
    self.description = description
    self.lvlcap = lvlcap
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


class knowledge:
  def __init__(self,name,description,attribute,effects,prereq):
    self.name = name
    self.description = description #What the knowledge is
    self.attribute = attribute #The attribute of the knowledge, ie fire, water earth air or etc
    self.effects = effects #what effects are caused by this 
    self.prereq = prereq #The proceeding skills that this is dependant on
    return 

def kmake():#This is the function for creating knowledge!!
  n=1
  while n ==1:
    knowledge_creator()
    n = int(input("put 1 to continue else put 0: "))
  return


def knowledge_creator(): 
  import pickle
  off = 0
  flag = 0
  db = []
  with open('knowledge_db.pkl','rb') as pickle_file:
    try:
      while 1:
        db.append(pickle.load(pickle_file))
    except EOFError:
      pass
  while off ==0:
    name = input('What is the name of this Knowledge?: ')
    for x in db:
      if x.name == name:
        flag = 1
        break
    if flag == 1:
      print("That knowledge already exists: ")
      continue
    attribute = input("What is the associated attribute? ")
    description = input("What should its description?: ")
    namedb = []
    tflag = 1
    while tflag==1:
      #This will produce effects for the skills and add them to the list
      alpha = effect_make()
      if alpha ==0:
        print("As noted the current effects are as above: ")
        while 1:
          namedb.append(input("what effect do you want?: "))
          if int(input("to stop press 1")) == 1:
            break
      else:
        namedb.append(alpha)
      tflag = int(input("put 1 to continue or 0 to stop"))
    for x in db:
      print(x.name)
    prereq = input("What is the prereq knowledge, seperate with spaces and if none then type NULL:  ")
    ktemp = knowledge(name,description,attribute,namedb,prereq)
    db.append(ktemp)

    off = 1
    print(db)
  with open('knowledge_db.pkl','wb') as pickle_file:
    for x in db:
      pickle.dump(x,pickle_file)
  return

def knowledge_read():
  import pickle
 #This function will print out the list of all creatures that exist in our data base
  with open('knowledge_db.pkl','rb') as pickle_file:
    print("This wizard currently has this set of knowledge: ")
    try:
      while 1:
        print(vars(pickle.load(pickle_file)))
    except EOFError:
      pass
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
    etemp = effects(name,description,lvlcap)
    db.append(etemp)
    off = 1
    #print(db)
  with open('effects_db.pkl','wb') as pickle_file:
    for x in db:
      pickle.dump(x,pickle_file)
  return namedb
