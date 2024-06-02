from dataclasses import dataclass
from api_functions import get_puuid

ARAM_QUEUE_CODE = 450

@dataclass
class Profile:
    realName: str
    gameName: str
    tagLine: str
    queue_code: str

    def __post_init__(self):
        self.puuid : str = get_puuid(self.gameName, self.tagLine)
        self.suffix: str = f"_{self.gameName}_{self.tagLine}"

ADRIEN = Profile('Adrien', 'Aram%20Bagarre', 'EUW', ARAM_QUEUE_CODE)
LEO = Profile('Leo', 'Nudibranchia', 'NUDI', None)