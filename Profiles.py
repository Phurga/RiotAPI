from dataclasses import dataclass
from api_functions import get_puuid

QUEUE_CODES = {'ARAM': 450, 'ALL' : None}

@dataclass
class Profile:
    realName: str
    gameName: str
    tagLine: str
    queue: str

    def __post_init__(self):
        self.puuid : str = get_puuid(self.gameName, self.tagLine)
        self.suffix: str = f"_{self.gameName}_{self.tagLine}"
        self.queue_code: str = QUEUE_CODES[self.queue]

ADRIEN = Profile('Adrien', 'Aram%20Bagarre', 'EUW', 'ARAM')
LEO = Profile('Leo', 'Nudibranchia', 'NUDI', 'ALL')
GASPAR = Profile('Gaspar', 'iSpip', 'EUW', 'ALL')