class creature:
  def __init__(self,name,Mp,Hp,skills,rare,drops = []):
    self.name = name
    self.Mp = Mp
    self.Hp = Hp
    self.skills = skills
    self.rare = rare
    self.drops = drops #Will be updated when materials are added from the materials section
    return


def cmake():#This is the function for creating monsters!!
  n=1
  while n ==1:
    creature_creator()
    n = int(input("put 1 to continue else put 0"))
  return


def creature_creator(): #This function will allow you to add new creatures to the creatures db
#Note that these are general creature types not specific entities
  import pickle
  off = 0
  flag = 0
  db = []
  with open('creature_db.pkl','rb') as pickle_file:
    try:
      while 1:
        db.append(pickle.load(pickle_file))
    except EOFError:
      pass
  while off ==0:
    name = input('What is the name of this type of Creature?: ')
    for x in db:
      if x.name == name:
        flag = 1
        break
    if flag == 1:
      print("That Creature already exists: ")
      continue
    MP = int(input("What should be the default Mana Pool of this Creature?: "))
    Health = int(input("What should be the default Health of this creature?: "))
    skills = []
    rare = int(input("What is the rarity of this creature by  default: "))
    while 1:
      skills.append(input("What is the skill that you would like to add?: "))
      skval =input("Would you like to add another skill?(y/n)")
      if skval == "y" or skval == "yes" or skval == "YES" or skval == "Yes":
        continue
      elif skval =="n" or skval == "NO" or skval == "no" or skval == "No":
        break
    ncreature = creature(name,MP,Health,skills,rare)
    db.append(ncreature)
    off = 1
    print(db)
  with open('creature_db.pkl','wb') as pickle_file:
    for x in db:
      pickle.dump(x,pickle_file)
  return

def creature_read():
  import pickle
 #This function will print out the list of all creatures that exist in our data base
  with open('creature_db.pkl','rb') as pickle_file:
    print("The creatures that are currently known to exist are listed as following: ")
    try:
      while 1:
        print(vars(pickle.load(pickle_file)))
    except EOFError:
      pass
  return