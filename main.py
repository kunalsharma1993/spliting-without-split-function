s = input("Type the string\n")
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
    
print("list is:", l)

# We can do it with split function also.

s = input("Type the string\n")
l = s.split(' ')
print("List is":, l)
