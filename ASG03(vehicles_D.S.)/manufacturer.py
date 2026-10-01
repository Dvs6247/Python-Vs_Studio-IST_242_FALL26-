class manufacturer:
    def __init__(self, name: str, country: str):
        self._name = name
        self._country = country
        """Added a class manufacturer to 
        use the function __init__ 
        for helping the class function
        and the function _init__ has two strings with self
        called name and country"""
        @property
        def get_name(self) -> str:
            return self._name
        @property
        def get_country(self) -> str:
            return self._country
"""Added @property class and getter to pull the country and name 
from this class to then be shown in the output"""
def __str__(self):
        return f"({self._name}, {self._country}"
"""Added __str__ function to 
return the name and country strings"""
