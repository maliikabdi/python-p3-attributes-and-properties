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
    # Using the global APPROVED_BREEDS for consistency
    approved_breeds = APPROVED_BREEDS

    def __init__(self, name="Doggo", breed="Beagle"):
        # Initialize the properties using the setters for validation
        self.name = name
        self.breed = breed

    # Getter and setter for the name property
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")
            self._name = "Doggo"  # Set to default name if invalid

    # Getter and setter for the breed property
    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value in Dog.approved_breeds:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")
            self._breed = "Beagle"  # Set to default breed if invalid
