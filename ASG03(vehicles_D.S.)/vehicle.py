from abc import ABC, abstractmethod

from manufacturer import Manufacturer
from auto_model import AutoModel

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
        
@property
def manufacturer(self) -> Manufacturer:
    return self._Manufacturer

@property
def model(self) -> AutoModel:
    return self._model

@property
def mpg(self) -> float:
    return self._mpg
"""Using @property classes 
for manufacturer, automodel, and mpg."""

@property
def release_year(self) -> int:
    return self._model.first_year

def how_far_with(self, num_of_gallons: int) -> float:
    return self._mpg * num_of_gallons
"""Added the how_far_with function using the Abstract method 
to then return self._mpg * num_of_gallons"""

def number_of_wheels(self) -> int:
    return 4
"""Added number_of_wheels function to return the integer 4
for now"""