from datetime import datetime
from datetime import timedelta
import sqlite3

from ClassClimber import Climber
from ClassMountain import Mountain

class Expedition:

    def __init__(self, id: int, name: str, mountain_id: int, start: str, date: datetime, country: str, duration: str, success: bool) -> None:
        self.id = id
        self.name = name
        self.mountain_id = mountain_id
        self.start = start
        self.date = date
        self.country = country
        self.duration = duration
        self.success = success

    def add_climber(self, climber: Climber):
        conn = sqlite3.connect('climbersapp.db')
        query = """
            INSERT INTO expedition_climbers (climber_id, expedition_id)
            SELECT ?, ?
            WHERE NOT EXISTS (SELECT 1 FROM expedition_climbers WHERE climber_id = ? AND expedition_id = ?)
        """

        conn.execute(query, [climber.id, self.id, climber.id, self.id])
        conn.commit()

    def get_climbers(self) -> list:
        conn = sqlite3.connect('climbersapp.db')
        cursor = conn.cursor()
        query = f"""
            SELECT * FROM climbers WHERE id IN (SELECT climber_id FROM expedition_climbers WHERE expedition_id = {self.id})
            """

        cursor.execute(query)

        people = cursor.fetchall()

        return people

    def get_mountain(self) -> Mountain:
        pass

    def convert_date(self, to_format: str) -> str:
        return datetime.strftime(self.date, to_format)

    def convert_duration(self, to_format: str) -> str:
        string = ''
        totalSeconds = 0
        containsMinutes = True

        if self.duration[-1].upper() == 'H':
            containsMinutes = False

        for char in self.duration:
            if char.isnumeric():
                string += char

            if char == 'H' or char == 'h':
                totalSeconds += int(string) * 3600
                string = ''
                continue

        if containsMinutes:
            totalSeconds += int(string) * 60

        convertedDuration = str(timedelta(seconds=totalSeconds))

        return convertedDuration

    def get_duration(self) -> str:
        return self.duration


    # Representation method
    # This will format the output in the correct order
    # Format is @dataclass-style: Classname(attr=value, attr2=value2, ...)
    def __repr__(self) -> str:
        return "{}({})".format(type(self).__name__, ", ".join([f"{key}={value!r}" for key, value in self.__dict__.items()]))

# date = datetime.strptime('1903-05-05', '%Y-%m-%d')

# expedition = Expedition(1, 'naam', 4, 'norgen', date, 'rusland', '2h', 1)

# print(expedition.get_climbers())
# print('test333')
