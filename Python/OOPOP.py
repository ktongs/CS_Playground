class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def speak(self,voice):
        print(voice + "!")

class Cat(Animal):
    def __init__(self,name,age,numLegs):
        Animal.__init__(self, name,age)
        self.numLegs = numLegs

cat = Cat("Kitty",10,4)

print("The cat name is " + cat.name + "and I have "+str(cat.numLegs)+" legs!")

dog = Animal('Bobby',10)

print("My dog name is " +dog.name+ "and I am "+str(dog.age)+" years old.")
dog.speak('bark')

dog.age = 50

print(dog.age)