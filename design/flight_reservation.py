import datetime
from typing import List

"""
Book a flight reservation service

A user can:
- view flights
- view his flights
- book his flights

Notes:
- Single type of seat for all planes
- Single type of plane with 100 seat configuration
- Worldwide users but only Air Canada

Criterias:
- Consistent
- Acceptable delay
- Accessibility
- 10 million daily active users
- 50 million total users

Servers Endpoints
-----------------

- POST /booking
    - flight_id
    - user_id
    - seat_id
    -> Booking (201)
    -x Seat not available (406)
    -x Flight cancelled (410)
"""

class User:
    id: int
    first_name: str
    last_name: str
    email: str
    phone_number: str
    address: str

class Flight:
    id: int
    plane_id: int
    departure_time: datetime.datetime
    arrival_time: datetime.datetime
    source: str
    destination: str
    seat_states: List['SeatState']

class Plane:
    id: int
    seats: List['Seat']
    accessibility: dict


class Seat:
    id: int
    plane_id: int
    type: str # {window, isle, middle, other}
    row: str
    column: str

class SeatState:
    id: int
    flight_id: int
    seat_id: int
    state: str # {unavailable, available, pending, taken}

class Booking:
    id: int
    user_id: int
    flight_id: int
    seat_id: int
