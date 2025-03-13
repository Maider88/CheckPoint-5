#1

for num in range(1, 11):
  print(num)

#2

def sum(x, y, d):
  return(x + y + d)

result = sum(1, 2, 3)
print(result)

#3

def sum(x, y, d):
  sum_lambda = lambda x, y, d: x + y + d
  return sum_lambda(x, y, d)

result = sum(1, 2, 3)
print(result)

#4

name = "Enrique"
list_names = ("Jessica", "Paul", "George", "Henry", "Adán")

if name in list_names:
  print(f" The name {name} is in the list")
else:
  print(f" The name {name} is not in the list")
