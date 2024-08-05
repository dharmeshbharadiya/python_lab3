class Animal:
    def eat(self):
        print("Eating...")

    def sleep(self):
        print("Sleeping...")

class Mammal:
    def walk(self):
        print("Walking...")

    def run(self):
        print("Running...")

class Dog(Animal, Mammal):
    def bark(self):
        print("Barking...")

    def fetch(self):
        print("Fetching...")
dog = Dog()
dog.eat()
dog.sleep()
dog.walk()
dog.run()
dog.bark() 
dog.fetch()