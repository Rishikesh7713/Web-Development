class parrot:
    species="bird"

def __init__(self,name,age):
    self.name=name
    self.age=age

blu=parrot("Blu", 10)
woo=parrot("Woo", 15)

print("Blu is a ",blu.species)
print("Woo is a ",woo.species)

print(blu.name," is ",blu.age," years old")
print(woo.name," is ",woo.age," years old")