from datetime import datetime

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

    def add_climber(climber: Climber):
        pass

    def get_climbers() -> list:
        pass

    def get_mountain() -> Mountain:
        pass

    def convert_date(to_format: str) -> str:
        pass

    def convert_duration(to_format: str) -> str:
        pass

    def get_duration() -> str:
        pass

    def get_climbers() -> dict:
        pass


    # Representation method
    # This will format the output in the correct order
    # Format is @dataclass-style: Classname(attr=value, attr2=value2, ...)
    def __repr__(self) -> str:
        return "{}({})".format(type(self).__name__, ", ".join([f"{key}={value!r}" for key, value in self.__dict__.items()]))
