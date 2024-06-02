from dataclasses import dataclass
from api_functions import get_puuid

QUEUE_CODES = {'ARAM': 450, 'CLASSIC': 420, 'ALL' : None}

@dataclass
class Profile:
    """Stores the key info about a lol player."""
    realName: str
    gameName: str
    tagLine: str # Can be found by looking on op.gg for instance
    queue: str # If 'ALL' is given, all queues will be looked after. See the QUEUE_CODES dict.

    def __post_init__(self):
        self.puuid : str = get_puuid(self.gameName, self.tagLine)
        self.suffix: str = f"_{self.gameName}_{self.tagLine}"
        self.queue_code: str = QUEUE_CODES[self.queue]

ADRIEN = Profile('Adrien', 'Aram%20Bagarre', 'EUW', 'ARAM')
LEO = Profile('Leo', 'Nudibranchia', 'NUDI', 'ALL')
GASPAR = Profile('Gaspar', 'iSpip', 'EUW', 'ALL')

TOUS = [ADRIEN, LEO, GASPAR]