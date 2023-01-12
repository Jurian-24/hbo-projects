from datetime import datetime, date
import sqlite3

class Climber:

    def __init__(self, id: int, first_name: str, last_name: str, nationality: str, date_of_birth: datetime) -> None:
        self.id = id
        self.first_name = first_name,
        self.last_name = last_name
        self.nationality = nationality
        self.date_of_birth = date_of_birth


    def get_age(self) -> int:
        now = date.today()
        return now.year - self.date_of_birth.year - ((now.month, now.day) < (self.date_of_birth.month, self.date_of_birth.day))


    def get_expeditions(self) -> list():
        conn = sqlite3.connect('climbersapp.db')
        query = "SELECT * FROM expeditions WHERE id IN (SELECT expedition_id FROM expedition_climbers WHERE climber_id = ?)"
        cursor = conn.cursor()
        cursor.execute(query, [self.id])
        expeditions = self.cursor.fetchall()

        return expeditions


    # Representation method
    # This will format the output in the correct order
    # Format is @dataclass-style: Classname(attr=value, attr2=value2, ...)
    def __repr__(self) -> str:
        return "{}({})".format(type(self).__name__, ", ".join([f"{key}={value!r}" for key, value in self.__dict__.items()]))
