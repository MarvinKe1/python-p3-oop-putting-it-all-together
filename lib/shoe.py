#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):  # ✅ Fixed: no space in __init__
        self.brand = brand
        self.size = size
        self.condition = "New"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

