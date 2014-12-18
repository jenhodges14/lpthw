from sys import exit

def gold_room():
  print "This room is full of gold. How many pieces of gold do you take?"
  print "Please enter your answer in numerical form with no letters or symbols."
  
  choice = int(raw_input("> "))
  
  if choice in range(0, 50): 
    print "Nice, you're not greedy, you win!"
    exit(0)
  elif choice > 50:
    dead("You greedy bastard.")
  else:
    dead("Man, learn to type a positive number.")
    
def bear_room():
  print "There is a bear here."
  print "The bear has a bunch of honey."
  print "The fat bear is in front of another door."
  print "How are you going to move the bear?"
  print "Take the honey or taunt the bear?"
  bear_moved = False
  
  while True:
    choice = raw_input("> ")
    
    if "honey" in choice:
      dead("The bear looks at you then slaps your face off.")
    elif "taunt" in choice and not bear_moved:
      print "The bear has moved from the door. You can go through it now. Type 'open' to open door."
      
      bear_moved = True
    elif "taunt" in choice and bear_moved:
      dead("The bear gets pissed off and chews your leg off.")
    elif "open" in choice and bear_moved:
      gold_room()
    else:
      print "I got no idea what that means."
      
def cthulhu_room():
  print "Here you see the great evil Cthulhu."
  print "He, it, whatever stares at you and you go insane."
  print "Do you flee for your life or eat your head?"
  
  choice = raw_input("> ")
  
  if "flee" in choice:
    start()
  elif "head" in choice:
    dead("Well that was tasty!")
  else:
    cthulhu_room()
    
def dead(why):
  print why, "Good job!"
  exit(0)
  
def start():
  print "You are in a dark room."
  print "There is a door to your right and left."
  print "Which one do you take?"
  
  choice = raw_input("> ")
  
  if choice == "left":
    bear_room()
  elif choice == "right":
    cthulhu_room()
  else:
    dead("You stumble around the room until you starve.")
    
start()
        