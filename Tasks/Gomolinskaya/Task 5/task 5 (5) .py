choice = input("Решение какой задачи вы хотите посмотреть :'1' '2' '3' \n ?" )

if  int(choice) == 1:
 l = ['0', '1', '2', '3', '4', '7', '8', '10']
 ranges = []
 for x in l:
    if not ranges:
        ranges.append([x])
    elif int(x)-prev_x == 1:
        ranges[-1].append(x)
    else:
        ranges.append([x])
    prev_x = int(x)
 final_ranges = ["-".join([r[0], r[-1]] if len(r) > 1 else r) for r in ranges]
 print(final_ranges)  

if  int(choice) == 2:
  l = ['4','7','10']
  ranges = []
  for x in l:
    if not ranges:
        ranges.append([x])
    elif int(x)-prev_x == 1:
        ranges[-1].append(x)
    else:
        ranges.append([x])
    prev_x = int(x)
  final_ranges = ["-".join([r[0], r[-1]] if len(r) > 1 else r) for r in ranges]
  print(final_ranges)  
 
if  int(choice) == 3:   
   l = ['2', '3', '8', '9']
   ranges = []
   for x in l:
    if not ranges:
        ranges.append([x])
    elif int(x)-prev_x == 1:
        ranges[-1].append(x)
    else:
        ranges.append([x])
    prev_x = int(x)
   final_ranges = ["-".join([r[0], r[-1]] if len(r) > 1 else r) for r in ranges]
   print(final_ranges)  
 