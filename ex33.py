# create variables
i = 0
numbers = []

# define functions
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
     
# begin the test    
testing(6, 2)