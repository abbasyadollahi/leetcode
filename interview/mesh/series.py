"""
You and I are working together to build the part of our team's application that will let users query about properties of series.

Users will be able to make requests like:
 - What is the Nth element of the series?
 - Is N a member of the series?
 - What is the smallest member of the series greater than N?

Examples of series:
 - Fibonacci numbers
 - prime numbers
 - n² - 2n

I will be working on the user interface, and you will be building the back-end library that my piece will call.
For the first release we only have to implement the "Is N a member of...?" question for the Fibonacci and prime number series,
although we will have to support both more queries and more series later, so the service needs to be extensible.
"""

"""
APIs:
- getNth(n, series) -> int
- isNMemberOfSeries(n, series) -> bool
- getSmallestMemberOfSeriesGreaterThanN(n, series) -> int

- getResultFromSeriesAndOperation(n, series, operation) -> Response

- getAllAvailableSeries() -> list[string]
- getAllAvailableOperations() -> list[dict]
"""


import logging
from abc import ABC
from dataclasses import dataclass
from functools import wraps
from typing import Any, Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")
OriginalFunction = Callable[P, R]
DecoratedFunction = Callable[P, R]


class Decorators:
    @staticmethod
    def create_cache(fun: OriginalFunction) -> DecoratedFunction:
        """Injects a cache into the first argument for series operations."""
        cache = {}

        @wraps(fun)
        def decorated(*args: P.args, **kwargs: P.kwargs) -> R:
            n, series, operation = args
            metrics = {"series": series, "operation": operation, "n": n}
            if n in cache:
                metrics["miss"] = False
                result = cache[n]
            else:
                metrics["miss"] = True
                result = fun(cache, *args, **kwargs)

            logging.info(metrics)
            return result

        return decorated

    @staticmethod
    def emit_request_metrics(fun: OriginalFunction) -> DecoratedFunction:
        """Emits metrics for series requests."""

        @wraps(fun)
        def decorated(*args: P.args, **kwargs: P.kwargs) -> R:
            _, n, series, operation = args
            logging.info({"series": series, "operation": operation, "n": n})
            return fun(*args, **kwargs)

        return decorated


class Series(ABC):
    @staticmethod
    def getNth(n: int) -> int:
        pass

    @staticmethod
    def isMember(n: int) -> bool:
        pass

    @staticmethod
    def smallestMember(n: int) -> int:
        pass


class Fibonacci(Series):
    """
    The `n`th sequence is equal to the sum of the `n - 1` and `n - 2` sequences.
    Base cases of `n`:
        - n = 0 => 1
        - n = 1 => 1
    """

    @staticmethod
    @Decorators.create_cache
    def getNth(cache: dict[int, int], n: int) -> int:
        i = 2
        n_2 = 1
        n_1 = 1
        current = 1
        for i in range(2, n):
            current = n_1 + n_2
            n_2 = n_1
            n_1 = current
            cache[i] = current

        return current


class Prime(Series): ...


@dataclass(frozen=True)
class Response:
    status: int
    data: dict[str, Any]
    schema: dict[str, type]


class Backend:
    SERIES = {"fibonacci": Fibonacci, "prime": Prime}

    @classmethod
    @Decorators.emit_request_metrics
    def getResultFromSeriesAndOperation(cls, n: int, series: str, operation: str) -> Response:
        result = getattr(cls.SERIES[series], operation)(n)
        return Response(200, {"n": n, "result": result}, {"n": int, "result": int})


Backend.getResultFromSeriesAndOperation(5, "fibonacci", "getNth")
