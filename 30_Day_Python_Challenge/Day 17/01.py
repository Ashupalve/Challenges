# Q1. Write a program that uses multiple inheritance to create a class `FlyingFish` from `Flyer` and
# `Swimmer` classes.

class Flyer:
    def fly(self):
        print("I can fly")
class Swimmer:
    def swim(self):
        print("I can swim")
class FlyingFish(Flyer, Swimmer):
    pass
ff = FlyingFish()
ff.fly()
ff.swim()