from auto_model import AutoModel

class AutoModel:
    def __init__(self,
                name:str,
                production:bool,
                years: list[int]):
        self._name = name
        self._production = production
        self.years = years
"""Created class AutoModel to call name, production, and years
in a different python file within the __init__ function"""
@property
def name(self) -> str:
          return self._name
  
@property
def production(self) -> bool:
        return self.production
      
@property
def years(self) -> list[int]:
          return self.years
"""Added @property as a class for name, production, and years
to call and then return that attribute"""