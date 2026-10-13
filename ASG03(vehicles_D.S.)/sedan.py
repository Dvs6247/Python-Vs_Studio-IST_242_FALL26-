from vehicle import Vehicle
from manufacturer import Manufacturer
from auto_model import AutoModel
"""Imported Vehicle, Manufacturer, and AutoModel packages
to have access from other files needed for Sedan.py"""

class Sedan(Vehicle):
    def __init__(self, manufacturer: Manufacturer,
                 model: AutoModel,
                 mpg: float):
        super().__init__(manufacturer, model, mpg)
"""Added Sedan Class with the __init__ function 
to call manufacturer, model, and mpg
using self"""

def number_of_wheels(self) -> int:
    return 4
"""Added number_of_wheels function 
to be called with self and return 4"""

def __str__(self):
    return f"({self._manufacturer}) {self._model}, mpg: {self._mpg:.2f}"
"""Added __str__ function with f" 
to return manufacturer, model, and mpg in format 
and with the use of self"""