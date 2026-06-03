class Load: # @TODO: insert load func to always be overloaded to load, then declare other load types
  def __init__(self, name: str, value: float):
    self.name = name
    self.value = value

  def __str__(self):
    return f"{self.name}: {self.value}"

class SimpleLoad(Load):
  def __init__(self, name: str, value: float):
    super().__init__(name, value)