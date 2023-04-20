n = [1, 2, 3, 4, 5, 6]
def p_even(n):
   even = [x for x in n if x % 2==0]
   res = sum(even)

   print(res)
   return res
    
p_even(n)