#The Database of the potential Knowledge Groups

plant_db_struct={
  'Name': 'Default',
  'Description':'Default',
  #'Magic Properties':[], for future implimentation
}

def pmake():#This is the function for creating monsters!!
  n=1
  while n ==1:
    plant_creator()
    n = int(input("put 1 to continue else put 0"))
  return


def plant_creator(): 
  import pickle
  off = 0
  flag = 0
  db = []
  with open('plant_db.pkl','rb') as pickle_file:
    try:
      while 1:
        db.append(pickle.load(pickle_file))
    except EOFError:
      pass
  while off ==0:
    name = input('What is the name of this Plant?: ')
    for x in db:
      if x['Name'] == name:
        flag = 1
        break
    if flag == 1:
      print("That Plant already exists: ")
      continue
    Description = input("What should its description?: ")
    ktemp = plant_db_struct
    ktemp['Name'] = name
    ktemp['Description'] = Description
    db.append(ktemp)
    off = 1
    print(db)
  with open('plant_db.pkl','wb') as pickle_file:
    for x in db:
      pickle.dump(x,pickle_file)
  return

def plant_read():
  import pickle
 #This function will print out the list of all creatures that exist in our data base
  with open('plant_db.pkl','rb') as pickle_file:
    print("The plants that are currently known to exist are listed as following: ")
    try:
      while 1:
        print(pickle.load(pickle_file))
    except EOFError:
      pass
  return