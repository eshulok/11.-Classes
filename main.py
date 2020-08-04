import turtle as t

#Let's create some classes
#Creatures will be the parent class
class Creatures:
  pass

#People is a child class of Creatures
class People(Creatures):
  pass

#Animals is also a child class of Creatures
class Animals(Creatures):
  def speak(self):
    print('animal sound')
  def move(self):
    print('animal on the move')
  def draw(self):
    pass
  
    
#Birds is a child class of Animals
class Birds(Animals):
  def lay_an_egg(self):
    print('I laid an egg!')
  
#Chickens is a child class of Birds
class Chickens(Birds):
  pass

#Let's create an object of the class Chickens
clucky = Chickens()

#We can use functions from its parent class
clucky.speak()
clucky.move()
clucky.lay_an_egg()

class Ducks(Birds):
  #Let's override the move and speak functions to be specific to this child class
  def move(self):
    print('swim swim')
  def speak(self):
    print('Quack Quack')

#Create an object of the Ducks class
ducky = Ducks()

#These will call the overridden functions from the Ducks class
ducky.speak()
ducky.move()

#The draw function in not overridden so it will look for the function in the parent class
ducky.draw()

#Note that objects from other classes with the same parent are not affected
clucky.speak()

#A child class that uses initializers
class Parrots(Birds):
  def __init__(self, name):
    self.name = name
  
  def speak(self):
    print("%s wants a cracker!" % self.name)

polly = Parrots("Polly")
polly.speak()

class Emus(Birds):
  def __init__(self, x, y):
    #Create a new Turtle pen
    self.pen = t.Turtle()
    #Move turtle to start position
    self.pen.up()
    self.pen.goto(x,y)
  def draw(self):
    self.pen.down()
    self.pen.circle(10)
    self.pen.right(80)
    self.pen.forward(50)
    self.pen.circle(20)
    self.pen.up()
    self.pen.circle(20, 90)
    self.pen.down()
    self.pen.right(120)
    self.pen.forward(80)
    self.pen.backward(80)
    self.pen.left(50)
    self.pen.forward(80)
  def move(self, distance):
    #First do the parent class move function
    Birds.move(self)
    #Now erase the previous emu location
    self.pen.reset()
    self.pen.up()
    #Move the pen the specified distance
    self.pen.backward(distance)
    #now draw the emu in the new location
    self.draw()
    
emmy = Emus(0,0)
emmy.speak()
emmy.draw()

oswald = Emus(-100,0)
oswald.draw()

emmy.move(50)
