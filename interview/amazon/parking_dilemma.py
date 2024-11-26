# https://www.hackerrank.com/x/library/hackerrank/all/questions/616680/view


def carParkingRoof(cars: list[int], k: int) -> int:
    cars.sort()
    num_cars = len(cars)

    l = 0
    r = k - 1
    smallest_roof = 1 + cars[r] - cars[l]

    while r < num_cars:
        smallest_roof = min(smallest_roof, 1 + cars[r] - cars[l])
        l += 1
        r += 1

    return smallest_roof
