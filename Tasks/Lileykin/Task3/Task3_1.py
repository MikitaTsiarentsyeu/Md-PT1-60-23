def vowels(string):
   
   dict = ['a','e','i','o','u','y']
   total = 0
  
   for s in range (len(string)):
      if (string[s] in dict):
         total += 1
   return total

string = input("input something\n")

print(vowels(string))