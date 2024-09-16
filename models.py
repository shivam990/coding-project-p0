from pydantic import BaseModel
from typing import List
from datetime import datetime

class Availability(BaseModel):
    start_time: datetime
    end_time: datetime

class UserAvailability(BaseModel):
    user_id: str
    availabilities: List[Availability]
