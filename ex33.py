# create variables
i = 0
numbers = []

# define functions
# define while loop function
def testing(number, increment):
  global i
  while i < number:
    print "At the top i is %d" % i
    numbers.append(i)
  
    i += increment
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i
  
  
    print "The numbers: "
  
    for num in numbers:
      print num
      
# define for loop and range function
def testing_for_loop():
  numbers = []
  for i in range(0, 6):
    numbers.append(i)
    
     
# begin the test  

# run with while loop function
testing(6, 2)
print numbers

# run with for loop and range function
testing_for_loop()
print numbers
