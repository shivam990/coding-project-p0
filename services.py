from models import UserAvailability, Availability
from typing import List, Optional
from datetime import datetime
from typing import List, Dict

# Mock database
user_availabilities = {}

# Helper function to check if two intervals overlap or are adjacent
def is_overlapping_or_adjacent(interval_1: Dict[str, str], interval_2: Dict[str, str]) -> bool:
    return interval_1['start_time'] <= interval_2['end_time'] and interval_2['start_time'] <= interval_1['end_time']

# Helper function to merge two overlapping or adjacent intervals
def merge_intervals(interval_1: Dict[str, str], interval_2: Dict[str, str]) -> Dict[str, str]:
    return {
        "start_time": min(interval_1["start_time"], interval_2["start_time"]),
        "end_time": max(interval_1["end_time"], interval_2["end_time"])
    }

# Function to merge overlapping intervals from a list
def merge_overlapping_intervals(availabilities: List[Dict[str, str]]) -> List[Dict[str, str]]:
    if not availabilities:
        return []
    
    # Sort intervals by start time
    availabilities.sort(key=lambda x: x["start_time"])
    
    merged_intervals = [availabilities[0]]
    
    for current in availabilities[1:]:
        last_merged = merged_intervals[-1]
        
        if is_overlapping_or_adjacent(last_merged, current):
            # Merge the current interval with the last merged interval
            merged_intervals[-1] = merge_intervals(last_merged, current)
        else:
            merged_intervals.append(current)
    
    return merged_intervals

# Function to save availability while merging intervals and skipping exact matches
def save_availability(user_id: str, new_availabilities: List[Dict[str, str]]) -> List[Dict[str, str]]:
    existing_availabilities = user_availabilities.get(user_id, [])
    
    # Combine new and existing availabilities
    all_availabilities = existing_availabilities + new_availabilities
    
    # Merge overlapping intervals
    merged_availabilities = merge_overlapping_intervals(all_availabilities)
    
    user_availabilities[user_id] = merged_availabilities
    print(f"Updated availability for {user_id}: {user_availabilities[user_id]}")
    return merged_availabilities

def get_availability(user_id: str) -> Optional[List[Availability]]:
    availabilities = user_availabilities.get(user_id, None)
    return availabilities
    
#     return overlap if overlap else None
def find_availability_overlap(user_id_1: str, user_id_2: str) -> Optional[List[Dict[str, str]]]:
    availabilities_1 = user_availabilities.get(user_id_1, [])
    availabilities_2 = user_availabilities.get(user_id_2, [])

    overlaps = []
    for a1 in availabilities_1:
        for a2 in availabilities_2:
            overlap_start = max(a1["start_time"], a2["start_time"])
            overlap_end = min(a1["end_time"], a2["end_time"])
            if overlap_start < overlap_end:
                overlaps.append({"start_time": overlap_start, "end_time": overlap_end})

    return overlaps if overlaps else None
