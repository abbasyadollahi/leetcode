"""
Design an ATM.

Assumptions:
- Software on a given machine
- Can be as many machines

Requirements:
- Pull out money
- Check your money
- Authenticate user

Non functional requirements:
- Consistency
- Reliable
- Latency < 1m
- Scalability

APIs:

Authenticate
- bank details
- atm location
- timestamp

ReadAccount
- bank details
- atm location
- timestamp

WithdrawAccount
- bank details
- atm location
- atm status
- atm location
- timestamp
"""

import datetime
from typing import Callable


def authenticate(func: Callable) -> Callable: ...


def emit_metrics(func: Callable) -> Callable: ...


class Event:
    id: int
    operation: str
    bank_details: str
    timestamp: datetime.datetime


class State: ...


class ATM:
    amount: int
    events: set[Event]
    state: State

    @authenticate
    @emit_metrics
    def read_account(self, bank_details: str, timestamp: datetime.datetime) -> str: ...

    @authenticate
    @emit_metrics
    def withdraw_account(self, bank_details: str, timestamp: datetime.datetime, amount: int) -> str:
        account = self.read_account(bank_details, timestamp)
        if account.checking.money > amount:
            start = self.check_cash()
            #  hardware.give_money(amount)
            end = self.check_cash()
            assert start - end == amount

    @authenticate
    @emit_metrics
    def deposit_account(self, bank_details: str, timestamp: datetime.datetime, amount: int) -> str:
        # check currency
        # real money
        # can we actually deposit
        # update the balance in bank
        # read account sum to validate response
        ...

    def state_options(self) -> State:
        # what is current state
        # give next state given that
        ...

    def event_dump(self) -> None: ...

    def check_cash(self) -> int:
        return self.amount
