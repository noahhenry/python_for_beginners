import random

for i in range(3):
  print(random.random())

# what if you want to limit the range of random numbers returned?
# use random.randint() and pass in the range...
for i in range(3):
  print(random.randint(10, 20))

members = ["John", "Marry", "Bob", "Mosh", "Noah"]
leader = random.choice(members)
print(leader)