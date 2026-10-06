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
def get_name(self) -> str:
          return self._name
  
@property
def get_production(self) -> bool:
        return self.production
      
@property
def get_years(self) -> list[int]:
          get_years = []
          if not get_years:
                 print("ValueError. The list is empty.")
          return self.years
"""Added @property as a class for name, production, and years
to call and then return that attribute
Returns the get_years as well with a ValueError 
when there is no list"""