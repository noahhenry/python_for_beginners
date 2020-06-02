numbers_list = [1,2,3,4,5,6,3,1,2,7,8,9,0,3]

for number in numbers_list:
  if numbers_list.count(number) > 1:
    numbers_list.remove(number)

print(numbers_list)


# how Mosh does it in tutorial
numbers_list2 = [1,2,3,4,5,6,3,1,2,7,8,9,0,3]
uniques = []

for number2 in numbers_list2:
  if number2 not in uniques:
    uniques.append(number2)

print(uniques)