from vehicle import Vehicle
from manufacturer import Manufacturer
from auto_model import AutoModel
"""Added packages Vehicle, Manufacturer, and AutoModel"""
class Truck(Vehicle):
    """Truck class with vehicle class properties"""
    def __init__(self, manufacturer: Manufacturer, 
                 model: AutoModel, mpg: float):
        super().__init__(manufacturer, model, mpg)
        """__init__ function using self
        for manufacturer, automodel, and mpg"""
        