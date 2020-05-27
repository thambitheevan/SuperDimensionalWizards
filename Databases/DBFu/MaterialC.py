material_db_struct = {
  "Name": "Name",
  "Value":0,
  "Weight":0,
  #"Magical Property":"blah",
  "Strength":0,
  "Source":"" 
  }

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
        strtmp = "Would you like to create a new material from: ",x,"if so type yes if not type no"
        temp = input(strtmp)
        if temp == "yes" or temp == "Yes" or temp == "YES":
          #Once magic properties are introduced add them here 
          mattemp = mattemp = {
  "Name": "Name",
  "Value":0,
  "Weight":0,
  #"Magical Property":"blah",
  "Strength":0,
  "Source":"" 
  }
          mattemp["Name"] = input("What is the name of the material? ")
          mattemp["Value"] = int(input("What is the value of this material: "))
          mattemp["Weight"] = int(input("What is the weight of this material: "))
          mattemp["Strength"] = int(input("What is the strength: ")) 
          mattemp["Source"] = x['Name']
          db.append(mattemp)

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
        
        strtmp = "Would you like to create a new material from: ",x,"if so type yes if not type no"
        temp = input(strtmp)
        if temp == "yes" or temp == "Yes" or temp == "YES":
          #Once magic properties are introduced add them here 
          mattemp = {
  "Name": "Name",
  "Value":0,
  "Weight":0,
  #"Magical Property":"blah",
  "Strength":0,
  "Source":"" 
  }
          mattemp["Name"] = input("What is the name of the material? ")
          mattemp["Value"] = int(input("What is the value of this material: "))
          mattemp["Weight"] = int(input("What is the weight of this material: "))
          mattemp["Strength"] = int(input("What is the strength: ")) 
          mattemp["Source"] = x['Name']
          db.append(mattemp)
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

def mmake():#this function will create materials from scratch 
  n=1
  while n ==1:
    material_creator()
    n = int(input("put 1 to continue else put 0"))
  return


def material_creator(): 
  import pickle
  off = 0
  flag = 0
  db = []
  with open('material_db.pkl','rb') as pickle_file:
    try:
      while 1:
        db.append(pickle.load(pickle_file))
    except EOFError:
      pass
  while off ==0:
    name = input('What is the name of this Material?: ')
    for x in db:
      if x['Name'] == name:
        flag = 1
        break
    if flag == 1:
      print("That material already exists: ")
      continue
    value = int(input("What is its value?: "))
    weight = int(input("What is its weight?: "))
    strength = int(input("What is its strength?: "))
    ktemp = material_db_struct
    ktemp["Name"] = name
    ktemp["Value"] = value
    ktemp["Weight"] = weight
    ktemp["Strength"] = strength
    db.append(ktemp)
    off = 1
    print(db)
  with open('material_db.pkl','wb') as pickle_file:
    for x in db:
      pickle.dump(x,pickle_file)
  return

def material_read():
  import pickle
 #This function will print out the list of all creatures that exist in our data base
  with open('material_db.pkl','rb') as pickle_file:
    print("The known materials are: ")
    try:
      while 1:
        print(pickle.load(pickle_file))
    except EOFError:
      pass
  return