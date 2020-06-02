# note: in python, you must define your function before you can call it.
def greet_user(first_name, last_name):
  print(f"Hi there, {first_name, last_name}!")
  print("welcome aboard, mate.")

print("Start")
greet_user("John", "Doe")
print("Finish")

# keyword arguments...
# if you want to pass the arguments out of order, you can do it like this:
greet_user(last_name="Hopes", first_name="Randy")
# ^^ it's not suggested that they are used like this, but keyword arguments can be helpful for readablity... i.e.
def calc_cost(price, shipping_rate, tax_rate):
  return (price + shipping_rate) * tax_rate

print(calc_cost(price = 10, shipping_rate = 5, tax_rate = 0.10)) # easier to read than bellow
print(calc_cost(10, 5, 0.10))

# ! also, keyword arguments should always come after positional arguments if used interchangeably.