# animal is-a object (yes, sort of confusing) look at the extra credit
class animal(object):
    pass


# dog is-a animal 
class dog(animal):
    def __init__(self, name):
        # __init__ has-a name
        self.name = name


# cat is-a animal
class cat(animal):
    def __init__(self, name):
        # __init__ has-a name
        self.name = name


# person is-a animal
class person(object):
    def __init__(self, name):
        self.name = name
        # person has-a pet of some kind
        self.pet = None


# employee is-a person
class employee(person):
    def __init__(self, name, salary):
        #
        super(employee, self).__init__(name)
        # employee has-a salary
        self.salary = salary


# fish is-a object
class fish(object):
    pass

# salmon is-a fish
class salmon(fish):
    pass

# halibut is-a fish
class halibut(fish):
    pass


# rover is-a dog
rover = dog("rover")

# satan is-a cat
satan = cat("satan")

# mary is-a person
mary = person("mary")

# mary的pet has-a satan
mary.pet = satan

# frank's salary is-a 12000
frank = employee("frank",12000)

# frank的pet has-a rover
frank.pet = rover

# flipper is-a fish
flipper = fish()

# crouse is-a salmon
crouse = salmon()

# harry is-a halibut
harry = halibut()