from functools import wraps
from inspect import getfullargspec
from typing import Any, Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")
OriginalFunction = Callable[P, R]
DecoratedFunction = Callable[P, R]


def provide(**provide_kwargs: int) -> Callable[[OriginalFunction], DecoratedFunction]:
    def decorator(fun: OriginalFunction) -> DecoratedFunction:
        fun_fullargspec = getfullargspec(fun)
        fun_args = fun_fullargspec.args
        fun_has_kwargs = fun_fullargspec.varkw is not None

        # Keep only the matching kwargs (Example 5)
        initial_kwargs = {
            arg_name: arg_value
            for arg_name, arg_value in provide_kwargs.items()
            if fun_has_kwargs or arg_name in fun_args
        }

        @wraps(fun)
        def decorated(*args: P.args, **kwargs: P.kwargs) -> R:
            # Allow overrides through args/kwargs (Example 4)
            merged_kwargs = {**initial_kwargs, **kwargs}
            for arg_name, _ in zip(fun_args, args):
                if arg_name in merged_kwargs:
                    del merged_kwargs[arg_name]

            return fun(*args, **merged_kwargs)

        return decorated

    return decorator


print("---------- Example 1 ----------")


@provide(a=2)
def add(a: int, b: int) -> int:
    return a + b


assert add(b=3) == 5

print("---------- Example 2 ----------")


@provide(a=2)
def add(a: int, b: int) -> int:
    return a + b


try:
    add(3)
    raise AssertionError
except TypeError:
    ...

print("---------- Example 3 ----------")


@provide(b=2)
def add(a: int, b: int) -> int:
    return a + b


assert add(3) == 5

print("---------- Example 4 ----------")


@provide(a=2)
def add(a: int, b: int) -> int:
    return a + b


assert add(3, 4) == 7
assert add(a=3, b=4) == 7

print("---------- Example 5 ----------")


@provide(ignore=123, b=1)
def add(a: int, b: int) -> int:
    return a + b


assert add(4) == 5

print("---------- Example 6 ----------")


@provide(a=2)
def add(a: int, b: int) -> int:
    """This adds 2 numbers."""
    return a + b


assert add.__name__ == "add"
assert add.__doc__ == "This adds 2 numbers."

print("---------- Example 7 ----------")


@provide(a=1, b=2)
def add(**kwargs: int) -> dict[str, Any]:
    return kwargs


assert add(c=3) == {"a": 1, "b": 2, "c": 3}
assert add(a=3, b=4) == {"a": 3, "b": 4}
