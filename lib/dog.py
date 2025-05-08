#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]


class Dog:
    def __init__(self, name="tom", breed="Chihuahua"):
        self.name = name
        self.breed = breed

    
    def get_breed(self):
        return self._breed

    
    def set_breed(self, value):
        if value in APPROVED_BREEDS:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")

    
    def get_name(self):
        return self._name

    
    def set_name(self, value):
        if not isinstance(value, str) or len(value) > 25 or value == "":
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = value

    
    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)
