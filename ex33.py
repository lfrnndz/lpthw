#i = 0
numbers = []

#while i < 6:
#   print(f"At the top i is {i}")
#   numbers.append(i)
#   
#   i = i + 1
#   print("Numbers now: ", numbers)
#   print(f"At the bottom i is {i}")
   
   
def while_func(counter, increment):
   i = 0
   while i < counter:
      print(f"At the top i is {i}")
      numbers.append(i)
      
      i += increment
      print("Numbers now: ", numbers)
      print(f"At the bottom i is {i}")
      
while_func(6, 1)

print("The numbers: ")

for num in numbers:
   print(num)
   
   

