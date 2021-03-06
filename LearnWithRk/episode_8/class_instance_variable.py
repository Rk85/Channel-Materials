class Dog:
    kind = 'canine'         # class variable shared by all instances
    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

d = Dog('Fido')
e = Dog('Buddy')

print(d.kind)
print(e.kind)
print(d.name)
print(e.name)

Dog.kind = "RK"
print(d.kind)
print(e.kind)

d.kind = "German sepherd"
print(d.kind)
print(e.kind)


d.name = "Rexy"
print(d.name)
print(e.name)
