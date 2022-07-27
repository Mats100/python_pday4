# Generating a random number
import random
random_list=[]

for i in range(0,5):
      n= random.randint(1,30)
      random_list.append(n)
      print(random_list)
# Reversing a string

dock=input("Enter a String:")
print("Reversed  String Value is:",dock[::-1])
