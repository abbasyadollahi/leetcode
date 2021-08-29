from typing import List


def trafficRide(lights: List[int], cycles: List[int], destinations: List[int]) -> int:
    time = 0
    location = 0
    lights_cycles = dict(zip(lights, cycles))

    for destination in destinations:
        while location != destination:
            time += 1
            if location not in lights_cycles or is_light_green(lights_cycles[location], time):
                if location < destination:
                    location += 1
                else:
                    location -= 1


def is_light_green(cycle: int, time: int) -> bool:
    return time % (2 * cycle) >= cycle
