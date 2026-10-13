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
    