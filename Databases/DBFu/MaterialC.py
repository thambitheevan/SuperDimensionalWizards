
class material:
  def __init__(self,name,value,weight,strength,skills,source):
    self.name =name
    self.value = value
    self.weight = weight
    self.strength = strength
    self.skills = skills
    self.source = source
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

def mat_true_make(): #This function will 
  import pickle
  ogdb = []
  db = []
  try:
    print("if you would like the cancel type 0")
    search = input("Do you want to input from Plants or Creatures: ")
  except:
    print("Invalid input")
    return
  if search == "Plant" or search == "plant" or search == "Plants" or search == "Plants":
    #This section will read through the plants and ask if you want to create a new material from them
    #flag = "Plants"
    with open('plant_db.pkl','rb') as pickle_file:
       try:
        while 1:
          ogdb.append(pickle.load(pickle_file))
       except EOFError:
          pass
    print("If you want to cancel at any point type 0")
    for x in ogdb:
      flag = 0
      while flag == 0:
        strtmp = "Would you like to create a new material from: ",x.name,"if so type yes if not type no"
        temp = input(strtmp)
        if temp == "yes" or temp == "Yes" or temp == "YES":
          #Once magic properties are introduced add them here 
          name = input("What is the name of the material? ")
          value = int(input("What is the value of this material: "))
          weight = int(input("What is the weight of this material: "))
          strength = int(input("What is the strength: ")) 
          source = x.name
          skills = x.skills #The total set of skill which can be attributed from the monster #Not all will occur
          db.append(material(name,value,weight,strength,skills,source))

        if temp == "no" or temp == "No" or temp == "NO":
          flag = 1
          continue
        if temp == "0":
          flag = 0
          continue
    with open('material_db.pkl','rb') as pickle_file:
      try:
        while 1:
          db.append(pickle.load(pickle_file))
      except:
        pass
    with open('material_db.pkl','wb') as pickle_file:  
      for x in db:
        pickle.dump(x,pickle_file)
    print("Process Completed")
    return
  if search == "Creatures" or search == "creature" or search == "Creature" or search == "creatures":
    #flag = "Creatures"
      #This section will read through the plants and ask if you want to create a new material from them
    #flag = "Plants"
    with open('creature_db.pkl','rb') as pickle_file:
       try:
        while 1:
          ogdb.append(pickle.load(pickle_file))
       except EOFError:
          pass
    print("If you want to cancel at any point type 0")
    for x in ogdb:
      print(db)
      flag = 0
      while flag == 0:
        
        strtmp = "Would you like to create a new material from: ",x.name,"if so type yes if not type no"
        temp = input(strtmp)
        if temp == "yes" or temp == "Yes" or temp == "YES":
          #Once magic properties are introduced add them here 
          name = input("What is the name of the material? ")
          value = int(input("What is the value of this material: "))
          weight = int(input("What is the weight of this material: "))
          strength = int(input("What is the strength: ")) 
          source = x.name
          skills = x.skills #The total set of skill which can be attributed from the monster #Not all will occur
          db.append(material(name,value,weight,strength,skills,source))
        if temp == "no" or temp == "No" or temp == "NO":
          flag = 1
          continue
        if temp == "0":
          flag = 0
          continue
    with open('material_db.pkl','rb') as pickle_file:
      try:
        while 1:
          db.append(pickle.load(pickle_file))
      except:
        pass
    with open('material_db.pkl','wb') as pickle_file:  
      for x in db:#Neeed to fix this why doesnt it work
        pickle.dump(x,pickle_file)
    print("Process Completed")
    return
  if search == "0":
    return
  else:
    print("That is an invalid search Protocol")
    mat_true_make()#Calls the function again for the user to try again
  return

def material_read():
  import pickle
 #This function will print out the list of all creatures that exist in our data base
  with open('material_db.pkl','rb') as pickle_file:
    print("The known materials are: ")
    try:
      while 1:
        print(vars(pickle.load(pickle_file)))
    except EOFError:
      pass
  return
