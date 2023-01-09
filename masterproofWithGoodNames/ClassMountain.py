import sqlite3

class Mountain:

    def __init__(self, id: int, name: str, country: str, rank: int, height: int, prominence: int, range: str) -> None:
        self.id = id,
        self.name = name
        self.country = country
        self.rank = rank
        self.height = height
        self.prominence = prominence
        self.range = range
        self.conn = sqlite3.connect('climbersapp.db')
        self.cursor = self.conn.cursor()

    def height_difference(self) -> int:
        return self.height - self.prominence

    def get_expeditions(self) -> list():
        query = "SELECT * FROM expeditions WHERE mountain_id = ?"
        self.cursor.execute(query, [self.id])
        expeditions = self.cursor.fetchall()

        return expeditions

    def get_height(self) -> int:
        return self.height

    def get_country(self) -> int:
        return self.country

    # Representation method
    # This will format the output in the correct order
    # Format is @dataclass-style: Classname(attr=value, attr2=value2, ...)
    def __repr__(self) -> str:
        return "{}({})".format(type(self).__name__, ", ".join([f"{key}={value!r}" for key, value in self.__dict__.items()]))
