#!/usr/bin/env python3

import os
from typing import TextIO

# If you add or upgrade any pip packages, please specify in `requirements.txt`
import yaml  # noqa

# Each Nest has this many Zips
NUM_ZIPS = 10

# Each Zip can carry between 1 and this many packages per flight
# Note: a Zip can deliver more than 1 package per stop
MAX_PACKAGES_PER_ZIP = 3

# Zips fly a constant groundspeed (m/s)
ZIP_SPEED_MPS = 30

# Zips can fly a total roundtrip distance (m)
ZIP_MAX_CUMULATIVE_RANGE_M = 160 * 1000  # 160 km -> meters

# The two acceptable priorities
EMERGENCY = "Emergency"
RESUPPLY = "Resupply"


# You shouldn't need to modify this class
class Hospital:
    def __init__(self, name: str, north_m: int, east_m: int) -> None:
        self.name = name
        self.north_m = north_m
        self.east_m = east_m

    @staticmethod
    def load_from_csv(f: TextIO) -> dict[str, "Hospital"]:
        """Reads and processes a CSV file object that conforms to the
        hospital.csv schema defined in README.md.

        Args:
            f (file_object): CSV file object to read into a dict.

        Returns:
            dict: Hospitals and their coordinates.
        """
        hospitals = {}
        for line in f.readlines():
            fields = [values.strip() for values in line.split(",")]
            name = fields[0]
            hospitals[name] = Hospital(
                name=name,
                north_m=int(fields[1]),
                east_m=int(fields[2]),
            )
        return hospitals


# You shouldn't need to modify this class
class Order:
    def __init__(self, time: int, hospital: Hospital, priority: str) -> None:
        self.time = time
        self.hospital = hospital
        self.priority = priority

    @staticmethod
    def load_from_csv(f: TextIO, hospitals: dict[str, Hospital]) -> list["Order"]:
        """Reads and processes a CSV file object that conforms to the
        orders.csv schema defined in README.md.
        Ok to assume the orders are sorted.

        Args:
            f (file_object): CSV file object to read into a dict.
            hospitals (dict): mapping of hospital name to Hospital objects

        Returns:
            list: Order objects.
        """
        orders = []
        for line in f.readlines():
            fields = [values.strip() for values in line.split(",")]
            orders.append(
                Order(
                    time=int(fields[0]),
                    hospital=hospitals[fields[1]],
                    priority=fields[2],
                )
            )
        return orders


# Feel free to extend as needed
class Flight:
    def __init__(self, launch_time: int, orders: list[Order]) -> None:
        self.launch_time = launch_time
        self.orders = orders

    def __str__(self) -> str:
        orders_str = "->".join([order.hospital.name for order in self.orders])
        return f"<Flight @ {self.launch_time} to {orders_str}>"


class ZipScheduler:
    def __init__(
        self,
        hospitals: dict[str, Hospital],
        num_zips: int,
        max_packages_per_zip: int,
        zip_speed_mps: int,
        zip_max_cumulative_range_m: int,
    ) -> None:
        self.hospitals = hospitals
        self.num_zips = num_zips
        self.max_packages_per_zip = max_packages_per_zip
        self.zip_speed_mps = zip_speed_mps
        self.zip_max_cumulative_range_m = zip_max_cumulative_range_m

        # Track which orders haven't been launched yet
        self._unfulfilled_orders: list[Order] = []

    @property
    def unfulfilled_orders(self) -> list[Order]:
        return self._unfulfilled_orders

    def queue_order(self, order: Order) -> None:
        """Add a new order to our queue.

        Note:
            Called every time a new order arrives.

        Args:
            order (Order): the order just placed.
        """

        self.unfulfilled_orders.append(order)

        # TODO: implement me!
        pass

    def launch_flights(self, current_time: int) -> list[Flight]:
        """Determines which flights should be launched right now.
        Each flight has an ordered list of Orders to serve.

        Note:
            Will be called periodically (approximately once a minute).

        Args:
            current_time (int): Seconds since midnight.

        Returns:
            list: Flight objects that launch at this time.
        """

        # TODO: implement me!
        # You should remove any orders from `self.unfulfilled_orders` as you go
        return []


class Runner:
    """A simulation runner that can playback order CSVs as if the day were
    progressing.
    """

    def __init__(self, hospitals_path: str, orders_path: str) -> None:
        with open(hospitals_path) as f:
            self.hospitals = Hospital.load_from_csv(f)

        with open(orders_path) as f:
            self.orders = Order.load_from_csv(f, self.hospitals)

        self.scheduler = ZipScheduler(
            hospitals=self.hospitals,
            num_zips=NUM_ZIPS,
            max_packages_per_zip=MAX_PACKAGES_PER_ZIP,
            zip_speed_mps=ZIP_SPEED_MPS,
            zip_max_cumulative_range_m=ZIP_MAX_CUMULATIVE_RANGE_M,
        )

    def run(self) -> None:
        """Run the simulator.
        This assumes any orders not fulfilled by the end of the day are failed.

        Note:
            This is a barebones implementation that should help get you
            started. You probably want to expand the runner's capabilities.
        """

        # Simulate time going from the first order time, until the end of the
        # day, in 1 minute increments
        sec_per_day = 24 * 60 * 60
        for sec_since_midnight in range(self.orders[0].time, sec_per_day):
            # Find and queue pending orders.
            self.__queue_pending_orders(sec_since_midnight)

            if sec_since_midnight % 60 == 0:
                # Once a minute, poke the flight launcher
                self.__update_launch_flights(sec_since_midnight)

        # These orders were not launched by midnight
        print(f"{len(self.scheduler.unfulfilled_orders)} unfulfilled orders at" + "the end of the day")

    def __queue_pending_orders(self, sec_since_midnight: int) -> None:
        """Grab an order from the queue and queue it.

        Args:
            sec_since_midnight (int): Seconds since midnight.
        """
        while self.orders and self.orders[0].time == sec_since_midnight:
            # Find any orders that were placed during this second and tell
            # our scheduler about them
            order = self.orders.pop(0)
            print(
                f"[{sec_since_midnight}] {order.priority} order received",
                f"to {order.hospital.name}",
            )
            self.scheduler.queue_order(order)

    def __update_launch_flights(self, sec_since_midnight: int) -> None:
        """Schedule which flights should launch now.

        Args:
            sec_since_midnight (int): Seconds since midnight.
        """
        flights = self.scheduler.launch_flights(current_time=sec_since_midnight)
        if flights:
            print(f"[{sec_since_midnight}] Scheduling flights:")
            for f in flights:
                print(f)


"""
Usage:

> python3 traveling_zip.py

Runs the provided CSVs.
"""
if __name__ == "__main__":
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    hospitals_path = os.path.join(root_dir, "inputs", "hospitals.csv")
    orders_path = os.path.join(root_dir, "inputs", "orders.csv")
    runner = Runner(
        hospitals_path=hospitals_path,
        orders_path=orders_path,
    )
    runner.run()
