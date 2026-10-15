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
          get_years = []
          if not get_years:
                 print("ValueError. The list is empty.")
          return list(self.years)
"""Added @property as a class for name, production, and years
to call and then return that attribute
Returns the get_years as well with a ValueError 
when there is no list"""

@property
def first_year(self) -> int:
       return self._years[0]

def __str__(self):
        return f"({self._name} = {self._production},{self._year}"