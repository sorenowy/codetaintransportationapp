from pydantic import BaseModel
from dataclasses import dataclass
from datetime import datetime

class Route(BaseModel):
    id: int
    start_location: str
    end_location: str
    price_per_km: float
    distance: float
    date_of_execution: datetime

@dataclass
class RouteRequestDTO:
    start_location: str
    end_location: str
    price_per_km: float
    distance: float
    date_of_execution: datetime