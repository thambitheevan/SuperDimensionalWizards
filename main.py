#This will read from the set of all monsters and be used to create bloodline Automatically from them the user will input the bloodline special effects

class bloodline:
  def __init__(self, name, maxpowerlevel, skills, value,success ,status=0):
    self.name = name
    self.maxpowerlevel = maxpowerlevel
    self.skills = skills #comes from the creatures skills
    #self.reqknowledge = reqknowledge #3 prereq + better chance and usage 
    self.value = value
    self.success = success #Chance of successful fusing
    self.value = value #Value of the bloodline
    self.status = status #Ability to transform into the creature 1->100 ie at 50 can transform fully but not use all of its abilities
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
  
def bmake():
  import pickle
  db = []
  cdb = []
  with open('bloodline_db.pkl','rb') as pickle_file:
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
  #Will first read across the creatures in order to find any that are not in the bloodline_db
  cflag = 0
  for x in cdb:
    for y in db:
      if x.name == y.name:
        cflag = 1
        break
    if cflag == 1:
      cflag = 0
      continue
    bname = x.name
    bmpl = float(x.Mp + x.Hp)/0.5 #Arbitrary function to be balanced later
    bskills = x.skills
    #Req Knowledge can be added here
    bval = x.rare*2
    bsucc = (float(x.rare) * bmpl)/100
    db.append(bloodline(bname,bmpl,bskills,bval,bsucc))
  with open('bloodline_db.pkl','wb') as pickle_file:
    for x in db:
      pickle.dump(x,pickle_file)
  return

def bloodline_read():
  import pickle
 #This function will print out the list of all bloodlines that exist in our data base
  with open('bloodline_db.pkl','rb') as pickle_file:
    print("The bloodlines that are currently known to exist are listed as following: ")
    try:
      while 1:
        print(vars(pickle.load(pickle_file)))
    except EOFError:
      pass
  return








  

