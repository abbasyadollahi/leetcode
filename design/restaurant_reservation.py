"""
Design me a restaurant reservation system.

1. Requirements gathering (functional and non-functional)
2. Define API
3. Estimations
4. Data model
5. High level design
6. Lower level for each component

Notes:
- 50 spots per restaurant
- 500_000 in Canada
- Every user has an account (500_000)
- 10% users are making a reservation at peak hour

Criteria
--------

- Consistency
- Availability

Servers Endpoints
-----------------

- Clients
    - make a reservation
    - cancel a reservation
    - search/view restaurants
    - login

- Restaurant
    - add my restaurants
    - update restaurants
    - manage reservations
"""


import datetime


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

# POST /api/restaurant
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
    table_ids: list[Table]

class Reservation:

    id: int # pk
    restaurant_id: int # fk
    reserved_at: datetime.datetime
    seats: int
