from abc import ABC

class Vehicle(ABC):
    """Using the Abstract Base Class type of class
    for all the vehicles in the code"""
    def __init__(self,
                 manufacturer: Manufacturer,
                 model: AutoModel,
                 mpg: float):

        self._manufacturer = manufacturer
        self._model = model
        self.mpg = mpg
"""Added __init__ function and 
using self to call specifically manufacture, model, and mpg"""
        
