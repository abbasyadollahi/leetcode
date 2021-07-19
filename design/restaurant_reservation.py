import datetime
from typing import List

"""
Design me a restaurant reservation system.

1. Requirements gathering (functional and non-functional)
2. Define API
3. Estimations
4. Data model
5. high-level design
6. lower-level for each component

# Spots per restaurant: 50
# 500_000 in Canada
# Every user has an account (500_000)
# During peak hours, 10% are making a reservation at peak hour
# 50_000 reservations at peak hour


Criterias
---------

- Clients
    - make a reservation
    - cancel a reservation
    - search/view restaurants
    - login

- Restaurant
    - add my restaurants
    - update restaurants
    - manage reservations

NFRs:
    - Consistency
    - Availability
"""

# POST /api/reservation
def make_reservation(
    user_id: int,
    restaurant_id: int,
    seats: int,
):
    return {
        "success": "all information relating to the reservation",
        "failure": "reason why it cannot make the reservation",
    }

# DELETE /api/reservation
def cancel_reservation(
    user_id: int,
    reservation_id: int,
):
    return {
        "success": "all information relating to the reservation + confirmation of cancellation",
        "failure": "reason why it cannot cancel the reservation + steps to contact restaurant",
    }

# POST /api/resturant
def add_restaurant(
    user_id: int,
    restaurant_name: str,
    restaurant_location: str,
    **details,
):
    return {
        "": ""
    }


class Location:
    id: int
    address: str
    postal_code: str


class Table:
    id: int
    seats: int
    accessibility: bool

class Restaurant:
    id: str
    location: Location
    table_ids: List[Table]

class Reservation:
    id: int # pk
    restaurant_id: int # fk
    reserved_at: datetime.datetime
    seats: int
