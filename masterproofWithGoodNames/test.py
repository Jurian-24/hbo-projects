from ClassClimber import Climber
from datetime import datetime

date_of_birth = datetime.strptime('03-04-2003', '%d-%m-%Y')

climber = Climber(1, 'Jurian', 'Andriessen', 'Dutch', date_of_birth)

print(climber.get_expeditions())
