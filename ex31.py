
# create functions
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
        
  elif go_on == "3":
    print "stop"
      
  elif go_on == "4":
    print "stop"
  else:
    print "stop"
   
  
  
def forward_or_not():
  forward = raw_input("> ")
    
  if forward == "1":
      print "You have now entered the hallway. There is a door that leads outside. There is an office that you can enter. There is a living room a few feet away."
      print "Would you like to enter any of the rooms, or stay here?"
      print "Press '1' for go through the dark blue door."
      print "Press '2' to go into the office."
      print "Press '3' to go into the living room."
      print "Press '4' to stay in the hallway."
      go_on_or_not()
      
  elif forward == "2":
      print "You want to explore the kitchen."
      print "What would you like to do?"
      print "Press '1' for look in the box on the island."
      print "Press '2' to look in the cupboard."
      print "Press '3' to look in the refrigerator."
      print "Press '4' to look in the drawer in the island."
      print "Press '5' to sit at the table."
      print "Press '6' to continue on into the home."
      
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
    print "You enter a the home of Mr. and Mrs. Hodges through the side door. You are standing in the kitchen. Which would you rather do?"
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
