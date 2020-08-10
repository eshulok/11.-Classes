import turtle as t

#Clases can have parent/child relationships

#Creature will be the parent class for several other classes
class Creature:
  #pass means we are intentionally not adding any functionality to the class right now
  pass

#Animals is also a child class of Creature
#An Animal is a kind of Creature
class Animal(Creature):
  def speak(self):
    print('animal sound')
  def move(self):
    print('animal on the move')
  def draw(self):
    pass
    
#Birds is a child class of Animal
#Birds are a kind of Animal
class Bird(Animal):
  def lay_an_egg(self):
    print('I laid an egg!')
  
#Chicken is a child class of Bird
class Chicken(Bird):
  pass

#Let's create an object of the class Chicken
clucky = Chicken()

#Let's put in a print statement to  make it easy to find the output for the following functions
print('Calling the speak, move and lay_an_egg functions for clucky the Chicken...')
#We can use functions from its parent class
clucky.speak()
clucky.move()
clucky.lay_an_egg()

class Duck(Bird):
  #Let's override the move and speak functions to be specific to this child class
  def move(self):
    print('swim swim')
  def speak(self):
    print('Quack Quack')

#Create an object of the Duck class
ducky = Duck()

print('Calling the speak and move functions for ducky the duck...')
#These will call the overridden functions from the Duck class
ducky.speak()
ducky.move()

#The draw function in not overridden so it will look for the function in the parent class, which has not been implemented
ducky.draw()

#Note that objects from other classes with the same parent are not affected
print("clucky still says: ")
clucky.speak()

#A child class that uses initializers
class Parrot(Bird):
  def __init__(self, name):
    self.name = name
  
  def speak(self):
    print("%s wants a cracker!" % self.name)

polly = Parrot("Polly")
print('Calling the speak function for polly the Parrot')
polly.speak()

class Emu(Bird):
  def __init__(self, x, y, color):
    #Create a new Turtle pen
    self.pen = t.Turtle()
    #Move turtle to start position
    self.pen.up()
    self.pen.goto(x,y)
    self.color = color
    
  def draw(self):
    self.pen.color(self.color)
    self.pen.down()
    self.pen.circle(10)
    self.pen.right(80)
    self.pen.forward(50)
    #Create a circle with 20 pixel radius and go around 450 degrees, not the default 360
    self.pen.circle(20, 450)
    self.pen.right(120)
    self.pen.forward(80)
    self.pen.backward(80)
    self.pen.left(50)
    self.pen.forward(80)
  def move(self, distance):
    #First do the parent class move function
    Bird.move(self)
    #Now erase the previous emu location
    self.pen.reset()
    self.pen.up()
    #Move the pen the specified distance
    self.pen.backward(distance)
    #now draw the emu in the new location
    self.draw()
    
emmy = Emu(0,0, 'brown')

print('Calling the speak and draw functions for emmy the Emu')
emmy.speak()
emmy.draw()

oswald = Emu(-100,0, 'blue')
oswald.draw()

print('Calling the move function for emmy the Emu')
emmy.move(50)
