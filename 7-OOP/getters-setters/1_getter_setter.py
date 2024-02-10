"""
Python Getter and Setter in class
"""


class Citizen:
    """
    Citizen class with name, and Province

    Represents the concept of `getters` and `setters` in python class.
    """

    def __init__(self, name: str, province: str) -> None:
        self.name = name
        self.province = province

    @property
    def province(self) -> str:
        """Getter -> Returns the province"""

        return self._province

    @province.setter
    def province(self, province: str) -> None:
        """Setter -> Sets the province"""

        if province.lower() not in ["punjab", "sindh", "kpk", "balochistan"]:
            raise ValueError(f"Province is not valid: {province}")
        self._province = province

    def __str__(self):
        return f"{self.name} is from {self.province.capitalize()}"


def get_citizen() -> tuple[str, str]:
    """
    Returns the name and province

    Takes no parameters

    Returns a tuple of the name and province
    """
    name = input("Name: ").strip()
    province = input("Province: ").strip()

    return name, province


NAME, PROVINCE = get_citizen()

citizen = Citizen(NAME, PROVINCE)

print(citizen)
