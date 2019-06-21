s = input("type the string\n")
buffer = ''
l = []

count = 0
for i in s:
  count += 1
  print(i, count, len(s))
  if i == ' ':
    l.append(buffer)
    buffer = ''  
  elif count == len(s) :
    buffer += i
    l.append(buffer)    
  else:
    buffer += i 
    
print("list:", l)
