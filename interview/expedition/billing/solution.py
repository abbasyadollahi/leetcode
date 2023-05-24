import calendar
import datetime
from typing import Annotated, Optional, TypedDict, TypeVar


class User(TypedDict):
    id: int
    """Id"""

    name: str
    """Name"""

    customer_id: int
    """Customer id"""

    activated_on: datetime.date
    """When this user activated their subscription"""

    deactivated_on: Optional[datetime.date]
    """When this user deactivated their subscription (inclusive)"""


class Subscription(TypedDict):
    id: int
    """Id"""

    customer_id: int
    """Customer id"""

    monthly_price_in_cents: int
    """Price per active user per month"""


def monthly_charge(month: Annotated[str, "YYYY-MM format"], subscription: Optional[Subscription], users: list[User]) -> int:
    """
    Computes the monthly charge for a given subscription.

    ### Returns
    The total monthly bill for the customer in cents, rounded to the nearest cent.
    For example, a bill of $20.00 should return 2000.
    If there are no active users or the subscription is `None`, returns 0.
    """

    # If there's no subscription then there's no fees incurred
    if subscription is None:
        return 0

    total_charge = 0
    month_start = datetime.datetime.strptime(month, '%Y-%m').date()
    month_end = last_day_of_month(month_start)

    for user in users:
        if user['customer_id'] != subscription['customer_id']:
            continue
        if user['activated_on'] > month_end:
            continue
        if user['deactivated_on'] is not None and user['deactivated_on'] < month_start:
            continue

        activated_on = user['activated_on']
        deactivated_on = user['deactivated_on'] or month_end

        activated_dates = min(deactivated_on, month_end) - max(activated_on, month_start)
        activated_dates += datetime.timedelta(days=1)

        total_dates = month_end - month_start
        total_dates += datetime.timedelta(days=1)

        percentage_of_activation = activated_dates / total_dates

        total_charge += (percentage_of_activation * subscription['monthly_price_in_cents'])

    return round(total_charge)


####################
# Helper functions #
####################

D = TypeVar('D', datetime.datetime, datetime.date)


def first_day_of_month(date: D) -> D:
    """
    Takes a datetime or date object and returns the same timestamp
    but with the day attribute changed to the first day of that month.
    For example:

    >>> first_day_of_month(datetime.date(2022, 3, 17))  # Mar 17
    datetime.date(2022, 3, 1)                           # Mar  1
    """
    return date.replace(day=1)


def last_day_of_month(date: D) -> D:
    """
    Takes a datetime or date object and returns the same timestamp
    but with the day attribute changed to last day of that month.
    For example:

    >>> last_day_of_month(datetime.date(2022, 3, 17))   # Mar 17
    datetime.date(2022, 3, 31)                          # Mar 31
    """
    last_day = calendar.monthrange(date.year, date.month)[1]
    return date.replace(day=last_day)


def next_day(date: D) -> D:
    """
    Takes a datetime or date object and returns the same timestamp
    but with one day added, which is the next day.
    For example:

    >>> next_day(datetime.date(2022, 3, 17))    # Mar 17
    datetime.date(2022, 3, 18)                  # Mar 18

    >>> next_day(datetime.date(2022, 3, 31))    # Mar 31
    datetime.date(2022, 4, 1)                   # Apr  1
    """
    return date + datetime.timedelta(days=1)
