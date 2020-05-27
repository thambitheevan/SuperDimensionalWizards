#Wizard System V2
#Converted from a Struct to a Class System OOP

class Wizard:
  def __init__(self,name,Senergy,Squality,Smodel,Mpool=100.0,Mprops=[0.0,0.0],knowledge=[],level=0,skills=[],truth=0,bloodline=["human"],body=0,clothing = [],health=1000):
    self.name = name
    self.Senergy = Senergy
    self.Squality = Squality
    self.Smodel = Smodel
    self.Mpool = Mpool
    self.Mprops = Mprops
    self.knowledge = knowledge
    self.level = level
    self.skills = skills
    self.truth = truth
    self.bloodline = bloodline
    self.body = body
    self.clothing = clothing
    self.health = health
    return
  def spirit_model_check(self):
    import math
    [Lval,nline] = self.line_check_V1()
    [Tval,ntriag] = self.triang_check_V1()
    MF = float(Lval) * 0.2 + math.log(float(ntriag)) #This is a very Arbitrary function pls balance the game
    #print(Tval," ",nline)
    delM = float(Tval)*0.05 + math.log(float(nline))

    self.Mprops[0] = MF
    self.Mprops[1] = delM
    return    
  def line_check_V1(self):
    smodel = self.Smodel
    Lval = 0
    nline=0
    blist=[]
    rlist=[4,9,14,19,24]
    dlist = [20,21,22,23,24]
    for x in range(len(smodel)):
        if x==0 and x not in blist:
            if x+2 not in rlist and x+1 not in rlist:#This method checks in the smodel struct along the horizontal for lines, taking into account the right limits and ensuring that any found values are added to the blist as such to avoid point reusing!!!!
                if smodel[x+1] ==0 and smodel[x+2] ==0:
                    if  smodel[x+3] ==0:
                        if x+4 in rlist and smodel[x+4] ==0:
                            Lval = Lval + 4
                            nline=nline+1
                            blist.append(x)
                            blist.append(x+1)
                            blist.append(x+2)
                            blist.append(x+3)
                            blist.append(x+4)
                            continue
                        Lval = Lval + 3
                        nline=nline+1
                        blist.append(x)
                        blist.append(x+1)
                        blist.append(x+2)
                        blist.append(x+3)
                        continue
                    Lval = Lval + 2
                    nline=nline+1
                    blist.append(x)
                    blist.append(x+1)
                    blist.append(x+2)
                    continue
            #blist = [] #This line can be uncommented to reset the blist  after Horizontal Check
            if x+5 not in blist and x+5 not in dlist and x+10 not in blist:#used for the horizontal checks
                if smodel[x+5]==0 and smodel[x+10] ==0:
                    if x+10 not in dlist and smodel[x+15]==0:
                        if x+15 not in dlist and smodel[x+20]==0:
                            Lval = Lval+4
                            nline=nline+1
                            blist.append(x)
                            blist.append(x+5)
                            blist.append(x+10)
                            blist.append(x+15)
                            blist.append(x+20)
                            continue
                        Lval = Lval+3
                        nline=nline+1
                        blist.append(x)
                        blist.append(x+5)
                        blist.append(x+10)
                        blist.append(x+15)
                        continue
                    Lval = Lval+2
                    nline=nline+1
                    blist.append(x)
                    blist.append(x+5)
                    blist.append(x+10)
                    continue
            if x+6 not in blist and x+6 not in dlist and x+6 not in rlist and x+12 not in blist:
                if smodel[x+6] ==0 and smodel[x+12] == 0:
                    if x+12 not in dlist and x+12 not in rlist and smodel[x+18] ==0:
                        if x+18 not in dlist and x+18 not in rlist and smodel[x+24]==0:
                            Lval = Lval+4
                            nline=nline+1
                            blist.append(x)
                            blist.append(x+6)
                            blist.append(x+12)
                            blist.append(x+18)
                            blist.append(x+24)
                            continue
                        Lval = Lval+3
                        nline=nline+1
                        blist.append(x)
                        blist.append(x+6)
                        blist.append(x+12)
                        blist.append(x+18)
                        continue
                    Lval = Lval+2
                    nline=nline+1
                    blist.append(x)
                    blist.append(x+6)
                    blist.append(x+12)
                    continue
    return [Lval,nline]				
  def triang_check_V1(self):
    smodel = self.Smodel
    Tval = 0
    ntriag = 0
    #needs to be limit debugged for this first set
    for x in range(len(smodel)):
        #This first algo checks for simple triangle
        if smodel[x] == 0:
            if x not in [4,9,14,19,24,20,21,22,23]:
              if smodel[x+1] == 0 and  smodel[x+5] == 0:
                  Tval = Tval +1
                  ntriag = ntriag+1
            if x<1:
                continue
            if smodel[x-1] == 0 and smodel[x+5] ==0:
                Tval = Tval +1
                ntriag = ntriag+1
            if x<5:
                continue
            if smodel[x+1] == 0 and  smodel[x-5] == 0:
                Tval = Tval +1
                ntriag = ntriag+1
            if smodel[x-1] == 0 and smodel[x-5] ==0:
                Tval = Tval +1
                ntriag = ntriag+1
                
        if smodel[x] ==0:#impliments for a 2 triangle
            if x in [0,1,2,5,6,7,10,11,12]:
                if smodel[x+1] ==0 and smodel[x+2] ==0 and smodel[x+5] ==0 and smodel[x+6] ==0 and smodel[x+10] ==0:
                    Tval = Tval +2
                    ntriag = ntriag+1
            if x in [24,23,22,19,18,17,14,13,12]:
                if smodel[x-1] ==0 and smodel[x-2] ==0 and smodel[x-5] ==0 and smodel[x-6] ==0 and smodel[x-10] ==0:
                    Tval = Tval +2
                    ntriag = ntriag+1
            if x in [2,3,4,7,8,9,12,13,14]:
                if smodel[x-1] ==0 and smodel[x-2] ==0 and smodel[x+5] ==0 and smodel[x+4] ==0 and smodel[x+10] ==0:
                    Tval = Tval +2
                    ntriag = ntriag+1
            if x in[22,21,20,15,16,17,10,11,12]:
                if smodel[x+1] ==0 and smodel[x+2] ==0 and smodel[x-5] ==0 and smodel[x-4] ==0 and smodel[x-10] ==0:
                    Tval = Tval +2
                    ntriag = ntriag+1
        if smodel[x] ==0: #For the 3 Triangle
            if x in[0,1,5,6]:
                if smodel[x+1] ==0 and smodel[x+2]==0 and smodel[x+3]==0 and smodel[x+7]==0 and smodel[x+11]==0 and smodel[x+5]==0 and smodel[x+10]==0 and smodel[x+15] ==0:
                    Tval = Tval +3
                    ntriag = ntriag+1
            if x in[24,23,19,18]:
                if smodel[x-1] ==0 and smodel[x-2]==0 and smodel[x-3]==0 and smodel[x-7]==0 and smodel[x-11]==0 and smodel[x-5]==0 and smodel[x-10]==0 and smodel[x-15] ==0:
                    Tval = Tval +3
                    ntriag = ntriag+1
        if smodel[x]==0:#accounts for the 4 Triangle
            if x in [0]:
                if smodel[x+1] == 0 and smodel[x+2] == 0 and smodel[x+3]==0 and smodel[x+4] ==0 and smodel[x+5] ==0 and smodel[x+10] ==0 and smodel[x+15] ==0 and smodel[x+20]==0 and smodel[x+16]==0 and smodel[x+12]==0 and smodel[x+8] ==0:
                    Tval = Tval +4;
                    ntriag = ntriag +1
            if x in [24]:
                if smodel[x-1] == 0 and smodel[x-2] == 0 and smodel[x-3]==0 and smodel[x-4] ==0 and smodel[x-5] ==0 and smodel[x-10] ==0 and smodel[x-15] ==0 and smodel[x-20]==0 and smodel[x-16]==0 and smodel[x-12]==0 and smodel[x-8] ==0:
                    Tval = Tval +4;
                    ntriag = ntriag +1
    return [Tval,ntriag]
  def check_level(self):
    lvlval = self.level;
    if lvlval == 0:
      level = "Mortal"
    if lvlval == 1:
      level = "Talent"
    if lvlval == 2:
      level = "Apprentice 1"
    if lvlval == 3:
      level = "Apprentice 2"
    if lvlval == 4:
      level = "Apprentice 3"
    if lvlval == 5:
      level = "Wizard 1"
    if lvlval == 6:
      level = "Wizard 2"
    if lvlval == 7:
      level = "Wizard 3"
    if lvlval == 8:
      level = "Wizard 4"
    if lvlval == 9:
      level = "Wizard 5"
    if lvlval >= 10:
      level = "Legendary Wizard"
    if self.truth == 1:
      level = "TruthFinder " +" "+ level
    print (level)
    return
  def kval(self):
    kval = 0
    try:
      for x in self.knowledge:
        kval = kval +1
    except:
      pass
    return kval 
  def detlevel(self):
    if self.Senergy == 50:
      Se = 2
    if (self.Senergy != 50) and (self.Senergy >= 25):
      Se = 1
    else:
      Se = 0
    Sq = round((((float(self.Squality))*(4))/(100)))
    k = self.kval()
    Mp = round((float(self.Mpool)*4)/1000)
    Mf = round((self.Mprops[0]*2)/5)
    lvl = Se+Sq+k+Mp+Mf
    self.level = lvl
    return


def Build_Wizard():
  import pickle
  #super temp script to let people try out the character building#
  print("Welcome to the Endless Plane")
  print("Your Journey is Currently Being Developed but Feel free to Roll your Wizarding Self")
  name = input('What is your Name? ')
  [Senergy,Squality] = gen_spirit()
  Smodel = build_spirit_model()
  Player = Wizard(name,Senergy,Squality,Smodel)
  Player.spirit_model_check()
  Player.detlevel()
  #Currently Saving all of this data in a textfile
  with open("save.pkl","wb") as pickle_file:
    pickle.dump(Player,pickle_file)
  return

def gen_spirit():
  from random import randint
  test = randint(0,20000)
  if test < 15000:
    Se = randint(10,18)
  if test >= 15000:
    Se = randint(18,25)
  Sq = randint(35,60)
  return [Se,Sq]

def build_spirit_model():
    smodel = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] #This is the default smodel
    cnt = 0 
    amt = 12 #The amount of points that one can place into their spirit model
    new_model =[]
    for x in range(len(smodel)):
        val = 2;
        while val not in [0,1]:
            if amt ==0:
                new_model.append(1)
                break
            print("You have:",amt,"0's Left")
            val = int(input(['Would you like place a 1 or a 0 ']))
            if val == 1:
                new_model.append(val)
                break
            if val ==0:
                new_model.append(val)
                amt = amt- 1
    return new_model

def player_read():
  import pickle
  with open("save.pkl","rb") as pickle_file:
    print(vars(pickle.load(pickle_file)))
  return

def save(Wizard):
  import pickle
  with open("save.pkl","wb") as pickle_file:
    pickle.dump(Wizard,pickle_file)
  return

def load():
  import pickle
  with open("save.pkl","rb") as pickle_file:
    rval=pickle.load(pickle_file)
  return rval