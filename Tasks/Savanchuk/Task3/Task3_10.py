#num = input("Введите числа:\n")
#num = num.split()
#max = 0
#list = []
#for i in num:
 #   if (int(i) % 2 != 0 and int(i) % 3 !=0 and int(i) !=1) or int(i) == 2 or int(i) == 3:
  #      list.append(i)
#for i in list:
 #   if int(i) > max:
  #      max = int(i)
#print(max)      

string=int(input("Enter the number and I'll show you some magic:\n "))

for i in range(2,string):
    k = 0
    for j in range(2,i-1):
        if i % j== 0:
            k=k+1
    if k == 0:
        print(f'All prime numbers before your number is: {i}')

#n = int(input("Введите числа:\n"))
#max = 0
#count = 0
#list = []
#n = n.split()
#for i in range(2, n):
 #   for j in range (2, i-1):
  #      if i % j == 0:
   #         count += 1 
    #if count == 0:
     #   list.append(i) 
#print(list)        
#for i in list:
 #   if i > max:
  #     max = i
#print(max)        