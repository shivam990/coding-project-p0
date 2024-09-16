from fastapi import FastAPI, HTTPException
from models import UserAvailability, Availability
from services import find_availability_overlap, save_availability, get_availability
from typing import List, Dict

app = FastAPI()

# Set availability
@app.post("/availability/{user_id}")
async def set_availability(user_id: str, availability: Dict[str, List[Dict[str, str]]]):
    if "availabilities" not in availability:
        raise HTTPException(status_code=400, detail="Invalid availability format. Expected a list of availabilities.")

    updated_availability = save_availability(user_id, availability["availabilities"])
    return {"availabilities": updated_availability}

# Show availability
@app.get("/availability/{user_id}")
async def show_availability(user_id: str):
    availability = get_availability(user_id)
    if availability:
        return {"availability": availability}
    raise HTTPException(status_code=404, detail="Availability not found!!")

# Find overlap between two users
@app.get("/overlap")
async def find_overlap(user_id_1: str, user_id_2: str):
    overlap = find_availability_overlap(user_id_1, user_id_2)
    if overlap:
        return {"overlap": overlap}
    raise HTTPException(status_code=404, detail="No overlapping availability found")
