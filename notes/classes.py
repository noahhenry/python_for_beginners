class Point:
  def move(self):
    print("move")

  def draw(self):
    print("draw")


point1 = Point() # instance of Point class
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1
print(point2.x)

# constructors
# ^ called when a new instance is created
class Point2:
  def __init__(self, x, y): # constructor function...
    self.x = x
    self.y = y

  def move(self):
    print("move")

  def draw(self):
    print("draw")

point = Point2(3, 5)
print(point.x)