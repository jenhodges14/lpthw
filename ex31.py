# create functions
def game_over():
  print "You have been kicked out and hospitalized. You cannot continue the game."
  print "Would you like to enter the home and begin again? Type 'yes' to continue, 'no' to remain outdoors, or simply close the browser to quit."
  begin_again = raw_input("> ")
  if begin_again == "yes":
    enter_or_not()
    
    

def choice():
  choice = raw_input("> ")
  if choice == "1":
    print "You have opened the top drawer in the desk. You find some old gum wrappers and a few paper clips. You steal a paper clip."
    print "You close the drawer."
    print "Mr. Mark catches you stealing a paper clip. He chases you out with a shotgun."
    print "You are now outside the house again. Would you like to enter?"
    enter_or_not()
  elif choice == "2":
    print "You have opened the bottom drawer in the desk. You find tax papers from 1987. You close the drawer again."
    print "Mrs. Cheryl enters the office."
    print "Mrs. Cheryl guides you back into the hallway."
    hallway()
  elif choice == "3":
    print "You take the bike out the side door and start to ride off down the driveway."
    print "Sassy, the white labrador retriever, chases you and you crash into a tree."
    print "Mr. Mark makes you pay him $500 for the bike that you have broken."
    print "And you end up in the hospital."
    game_over()
  elif choice == "4":
    hallway()
  else:
    print "You are mentally insane. You have entered the insane asylum. Mr. Mark finally called the popo to come take you away."
    print "Would you like to begin again? Type 'yes' to enter the home, 'no' to remain outdoors, or simply exit the browser to quit."
    enter_or_not()
    
    
   
def go_on_or_not():
  go_on = raw_input("> ")
  if go_on == "1":
    print "You go through the dark blue door on your right. You are back outside. The birds are singing. It looks like it might rain soon."
    print "You walk around to the side door where you first entered the home."
    print "Would you like to enter the home again?"
    enter_or_not()
  elif go_on == "2":
    print "You choose to go into the office. It's a mess. What would you like to do?"
    print "Press '1' if you would like to open the top drawer on the desk."
    print "Press '2' if you would like to open the bottom drawer on the desk."
    print "Press '3' if you would like to take the bike in the corner for a ride."
    print "Press '4' if you would like to exit into the hallway."
    choice()
  elif go_on == "3":
    print "You have chosen to enter the living room."
    print "You sit down with Mr. Mark and Mrs. Cheryl. They give you ice cream and cookies. You have won the game."
    print "Would you like to enter the home and begin again? Type 'yes' to enter the home, 'no' to remain outdoors, or simply exit the browser to quit."
    enter_or_not()
  elif go_on == "4":
    print "You have chosen to stay in the hallway."
    print "You admire the chandelier above your head."
    hallway()
  else:
    print "You are mentally insane. You have entered the insane asylum. Mr. Mark finally called the popo to come take you away."
    print "Would you like to begin again? Type 'yes' to enter the home, 'no' to remain outdoors, or simply exit the browser to quit."
    enter_or_not()
  
  
  
def hallway():
  print "You have now entered the hallway. There is a door that leads outside. There is an office that you can enter. There is a living room a few feet away."
  print "Would you like to enter any of the rooms, or stay here?"
  print "Press '1' for go through the dark blue door."
  print "Press '2' to go into the office."
  print "Press '3' to go into the living room."
  print "Press '4' to stay in the hallway."
  go_on_or_not()
  
  

def kitchen():
  kitchen_choice = raw_input("> ")
  if kitchen_choice == "1":
    print "You look in the box on the island. There is fresh, homemade gluten-free bread."
    print "Mrs. Cheryl walks into the room and tells you about MSG and porphyria."
    print "You are inspired to become a biochemist."
    print "You immediately leave, sign up for college, and pursue your career."
    print "Good job!"
    print "Would you like to begin the game again? Type 'yes' to enter the home, 'no' to stay outside the home, or simply exit the browser to quit."
    enter_or_not()
  elif kitchen_choice == "2":
    print "You want to look in the cupboard. There are gingerbread cookies and coffee."
    print "You make yourself and Mr. Mark a cup of coffee, and you talk about the honeybees that he has outdoors."
    print "You decide to become a beekeeper."
    print "You go outside with him and learn to work with bees."
    print "You go wild and decide to live like John the Baptist."
    print "You live in the fields of Washington County, eating wild honey and locusts."
    print "Would you like to begin the game again? Type 'yes' to enter the home, 'no' to stay outside the home, or simply exit the browser to quit."
    enter_or_not()
  elif kitchen_choice == "3":
    print "You decide to look in the refrigerator. There is some grass-fed beef and raw milk from South Carolina."
    print "You drink the raw milk, discover it has turned into cheese and mold, and die on the spot."
    print "Would you like to begin the game again? Type 'yes' to enter the home, 'no' to stay outside the home, or simply exit the browser to quit."
    enter_or_not()
  elif kitchen_choice == "4":
    print "You would like to continue through the home."
    print "You enter the hallway."
    hallway()
  else:
    print "You have selected an incorrect choice. Mrs. Cheryl takes you to the insane asylum."
    print "Would you like to begin the game again? Type 'yes' to enter the home, 'no' to stay outside the home, or simply exit the browser to quit."
    enter_or_not()
    

  
def forward_or_not():
  forward = raw_input("> ")
  if forward == "1":
      hallway()
  elif forward == "2":
      print "You want to explore the kitchen."
      print "What would you like to do?"
      print "Press '1' for look in the box on the island."
      print "Press '2' to look in the cupboard."
      print "Press '3' to look in the refrigerator."
      print "Press '4' to continue on into the home."
      kitchen()
      
  elif forward == "3":
      print "You are leaving the home."
      print "Would you like to enter the home?"
      enter_or_not()
  else:
      print "You are mentally insane. If you want to stay out of the mental institution, please select '1', '2' or '3' to explore the home."
      forward_or_not()
  
  

def enter_or_not():
  print "Type 'yes' to enter. Type 'no' to stay where you are. (case-sensitive) Hit enter after entering the answer."
  enter = raw_input("> ")
  if enter == "yes":
    print "You enter the home of Mr. and Mrs. Hodges through the side door. You are standing in the kitchen. Which would you rather do?"
    print "1. Go forward into the hallway."
    print "2. Stay and explore the kitchen."
    print "3. Go back outside."
    print "Type in either number, then hit 'enter'."
    forward_or_not()
  elif enter == "no":
    print "You remain sitting on the concrete porch outside. It's a beautiful day. However, you had better go in and speak, or Mr. and Mrs. Hodges may think you are a stalker."
    print "Would you like to go in?"
    enter_or_not()
  else:
    print "You are mentally insane. If you want to stay out of the mental institution, please select 'yes' or 'no' to enter the home."
    enter_or_not()
  
  
  
# begin the game
print "Welcome to the Hodges' residence! Would you like to enter?"
enter_or_not()
