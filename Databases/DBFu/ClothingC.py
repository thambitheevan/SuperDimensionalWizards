#Holds all of the clothing values in a list of dict's
class clothing:
  def __init__(self, name, material,slot, weight=0,  strength=0,value=0):
  #Head, Neck, Body, Legs, Belt, Feet, Hands1,Hands2, Ring1,Ring2
    self.name = name
    self.material = material
    self.weight = weight
    self.slot = slot
    self.strength = strength
    self.value = value
  def clothing_update(self):
    import pickle
    matdb = []
    if self.slot == "Head":
      Sval = 10.0
    if self.slot == "Body":
      Sval = 20.0
    if self.slot == "Legs":
      Sval = 12.0
    if self.slot == "Feet":
      Sval = 5.0
    with open('material_db.pkl','rb') as pickle_file:
      try:
        while 1:
          matdb.append(pickle.load(pickle_file))
      except:
        pass
    for x in matdb:
      if x["Name"] == self.material:
        matstr = x["Strength"]
        matweight = x["Weight"]
        matvalue = x["Value"]
    self.weight = matweight * Sval/100
    self.strength = matstr * Sval
    self.value = matvalue*Sval/2
    return 
    
def clothing_make():
  import pickle
  db = []
  matdb = []
  flag = 0
  with open('clothing_db.pkl','rb') as pickle_file:
    try:
      while 1:
        db.append(pickle.load(pickle_file))
    except:
      pass
  with open('material_db.pkl','rb') as pickle_file:
    try:
      while 1:
        matdb.append(pickle.load(pickle_file))
    except:
      pass
  while flag ==0:
    name = input("What is the name of this piece of Clothing?: ")
    tempflag = 0
    while tempflag == 0:
      print (matdb)
      material = input("What is the name of the material?: ")
      for x in matdb:
        if material == (x['Name']):
          tempflag = 1
          break
    while 1:
      slots = ["Head", "Neck", "Body", "Legs", "Belt", "Feet", "Hands1","Hands2","Ring1","Ring2"]
      print(slots)
      slot = input("What slot would you like for this article?: ")
      if slot in slots:
        break
      print("Invalid Slot try again")

    cloth = clothing(name,material,slot)
    cloth.clothing_update()
    db.append(cloth)
    while 1:
      check = input("If you would like to continue type yes and if not type no")
      if check.lower == "yes":
        flag = 0
        break
      else:
        flag = 1
        break
  with open('clothing_db.pkl','wb') as pickle_file:
    for x in db:
      pickle.dump(x,pickle_file)
  return

def clothing_read():
  import pickle
 #This function will print out the list of all creatures that exist in our data base
  with open('clothing_db.pkl','rb') as pickle_file:
    print("The clothing that are currently known to exist are listed as following: ")
    try:
      while 1:
        print(pickle.load(pickle_file).name)
    except EOFError:
      pass
  return

def clothing_investigate():
  import pickle
 #This function will print out the list of all creatures that exist in our data base
  flag = 0
  db = []
  with open('clothing_db.pkl','rb') as pickle_file:
    print("The clothing that are currently known to exist are listed as following: ")
    try:
      while 1:
        db.append(pickle.load(pickle_file))
    except EOFError:
      pass
    for x in db:
      print(x.name)
    while flag == 0:
      val = input("which Clothing would you investigate: ")
      for x in db:
        print (x.name,val)
        if x.name == val:
          print (vars(x))
          return
        else:
          continue
      if flag == 0:
        print("Invalid Name")
      
        

  return