# Activity 2: Polymorphism Challenge! 🎭

class Animal:
    def move(self):
        print("This animal moves in its own way.")

class Dog(Animal):
    def move(self):
        print("Running 🐕")

class Bird(Animal):
    def move(self):
        print("Flying 🐦")

class Fish(Animal):
    def move(self):
        print("Swimming 🐟")

# Example usage
animals = [Dog(), Bird(), Fish()]

for animal in animals:
    animal.move()

