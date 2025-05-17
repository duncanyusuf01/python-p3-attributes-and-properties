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
    approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", "French Bulldog", "Pug", "Pointer"]
    def __init__(self,name="Victor", breed="cheater"):
        if isinstance(name, str) and 1<=len(name)<=25:
            self.name=name

            if breed in Dog.approved_breeds:
                self.breed=breed
            else:
                print("Breed must be in list of approved breeds.")
                self.breed=None
        else:
            print("Name must be string between 1 and 25 characters.")
            self.name=None
        