

class AutoModel:
    def __init__(self, name:str, production:bool, years: list[int]):
        self._name = name
        self._production = production
        self.years = years

        