#This will be recast in the gameplay however this will allow the first set of knowledge to compile

#In order to introduce gameplay elements we use these loops and will call them in the main loop

def intro(): #This handles the initial part of the game
  print("Welcome to the endless Plane")
  name = input("\n What is your name? ")
  flag = [0, 0, 0]
  while 1:
    local = ["city","village","farm","forest"]
    print(local)
    temp0 = input("Where did you grow up?: ").lower()
    if temp0 not in local:
      print("invalid location")
      continue
    if temp0 == local[0]:
      print("Growing up in the city you had many opportunities and many difficult roads \n")
      flag[0] = 0
    if temp0 == local[1]:
      print("A small village is a great place to grow up, yet you have always found it boring\n")
      flag[0] = 1
    if temp0 == local[2]:
      print("your family has always provided, you have grown up surrounded by animals and food, however farmers have many hard times aswell\n")
      flag[0] = 2
    if temp0 == local[3]:
      print("Growing up surrounded by the trees and wild animals, you learned the harsh realities of nature and the true beauty of the world\n")
      flag[0] = 3
    break
  if flag[0] == 0:
    print("Your father worked in what role in the city?: ")
    print("0: a Merchant\n 1: a Servant \n 2: a city guard \n 3: The Magistrate\n")
    while 1:
      flag[1] = int(input("(Input the number)"))
      if flag[1] in [0,1,2,3]:
        break
  if flag[0] == 1:
    print("Your father always a hardworking man lived as a: ")
    print("0: Blacksmith\n 1: Shopkeeper \n 2: A Warrior \n 3: The village elder")
    while 1:
      flag[1] = int(input("(Input the number)"))
      if flag[1] in [0,1,2,3]:
        break 
  if flag[0] == 2:
    print("life on the farm was hard but surrounded by family, you mostly took to helping which member of your family: ")
    print("0: Your Brother who was in charge of the crops\n 1: Your Mother and her tasks taking care of the family and the animals\n 2: Your uncle who would defend the farm and the animals from raiders and wild animals \n 3: your father going over the farming records and heading to the market with the goods")
    while 1:
      flag[1] = int(input("(Input the number)"))
      if flag[1] in [0,1,2,3]:
        break 
  if flag[0] == 3:
    print("Living in the forest and off of the land is difficult, your father and yourself survived by: ")
    print("0: Poaching animals\n 1: Exploring ancient ruins for their artifacts \n 2: pilaging and raiding towns and caravans  \n 3: Fishing and gathering in the great rivers")
    while 1:
      flag[1] = int(input("(Input the number)"))
      if flag[1] in [0,1,2,3]:
        break 
  print("Your old life will be coming to an end soon, you found out that a strange old man known to some as a magical being is coming to town\n")
  print("You know that this is the best way to a better life")
  if flag[0] == 0:
    print("You quickly head to the government building where a small line of other young teenagers have gathered")
  if flag[0] == 1:
    print("The wizard seems to be here looking for a specific item, you follow them through the village market dodging from stall to stall")
  if flag[0] == 2:
    print("The wizard is passing through by your farm and as you stand at the doorway you see your father greeting him and inviting him inside of your home")
  if flag[0] == 3:
    print("The wizard will be coming down the forest road, you wait patiently at the side...")
    print('\n')
    print("The wizards cart comes to a halt just where you are waiting by at the side of the road")
  print("...\n...\n...\n")
  print("Without even realising it the wizard appears in front of you\n This man wearing a clean black suit with a white shirt, he was wearing a simple top hat and in his hand in a cane with what appears to be the head of a dragon fashioned from gold atop its peak.\n without saying a word the mystical man pulled a small orb out of his ring")
  print("The man simply said 'choose one object'\n and suddenly the area all around ",name," was replaced with a strange darkness\n, as the small amount of light came into focus ",name," saw four objects floating and filling up the space \n" )
  print("The first was a small red ball, perfectly round and with a red that seemed almost like flowing blood\n The next object was a small necktie, one that might be worn by a gentleman such as the wizard that had been in front of ",name," only a moment ago, it was deep blue as if looking into the depths of the ocean\n")
  print("The third item was a small cube, it was a deep dark black as such that no light could escape it, while the cube was very small it seemed to pull ",name," into it\n the final object on the table was a simple glass vial, the top was closed with a small cork but as ", name, "gazed into it nothing could be seen")
  while 1:
    flag[2] = int(input("which of these objects do you choose?: \n 1: The Ball\n 2: The Necktie\n 3: The Block\n 4: The Vial\n"))
    if flag[2] in [0,1,2,3]:
        break
  return [name,flag]
