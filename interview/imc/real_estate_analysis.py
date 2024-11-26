import bisect
import statistics
from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Analysis:
    comparisons: list[int]
    average: float | None
    standard_deviation: float | None
    absolute_difference: float | None
    outlier: bool


def findValuation(reqArea: int, areas: list[int], prices: list[int]) -> int:
    candidates = generateCandidates(areas, prices)

    if not candidates:
        return 1000

    if len(candidates) == 1:
        (_, price), _ = candidates.popitem()
        return formalize_price(price)

    comparisons_by_area = defaultdict(list)
    for area, price in candidates:
        comparisons_by_area[area].append(price)

    if reqArea in comparisons_by_area:
        return formalize_price(statistics.fmean(comparisons_by_area[reqArea]))

    areas = sorted(comparisons_by_area.keys())

    if reqArea < areas[0]:
        i = 0
    elif reqArea > areas[-1]:
        i = -2
    else:
        i = bisect.bisect_right(areas, reqArea) - 1

    x1, y1 = areas[i], statistics.fmean(comparisons_by_area[areas[i]])
    x2, y2 = areas[i + 1], statistics.fmean(comparisons_by_area[areas[i + 1]])

    return formalize_price(extrapolate(reqArea, x1, y1, x2, y2))


def generateCandidates(areas: list[int], prices: list[int]) -> dict[tuple[int, int], Analysis]:
    """
    Generate all candidates and remove the outliers.
    """

    houses = list(zip(areas, prices))
    candidates = {
        house: Analysis(
            comparisons=[],
            average=None,
            standard_deviation=None,
            absolute_difference=None,
            outlier=False,
        )
        for house in houses
    }

    for i, (area, price) in enumerate(houses):
        for j, (other_area, other_price) in enumerate(houses):
            if area == other_area and i != j:
                candidates[(area, price)].comparisons.append(other_price)

    for (area, price), analysis in candidates.items():
        if not analysis.comparisons:
            continue

        analysis.average = statistics.fmean(analysis.comparisons)
        analysis.standard_deviation = statistics.pstdev(analysis.comparisons) if len(analysis.comparisons) > 1 else 0
        analysis.absolute_difference = abs(price - analysis.average)
        analysis.outlier = analysis.absolute_difference > 3 * analysis.standard_deviation

    candidates = {house: analysis for house, analysis in candidates.items() if not analysis.outlier}

    return candidates


def extrapolate(x: int, x1: int, y1: int, x2: int, y2: int) -> float:
    """
    Extrapolate the price of a house given its area.
    """

    return y1 + (x - x1) * (y2 - y1) / (x2 - x1)


def formalize_price(price: float) -> int:
    """
    Round to nearest integer and limit to 10^3 and 10^6.
    """

    price = max(price, 10**3)
    price = min(price, 10**6)
    return round(price)


print(
    findValuation(
        1500,
        [1200, 1300, 1200, 1300, 1200, 2000],
        [12000, 24000, 14000, 22000, 13000, 30000],
    )
)

print(
    findValuation(
        1200,
        [1500, 500, 1000, 2000, 2500],
        [30000, 10000, 20000, 40000, 50000],
    )
)

print(
    findValuation(
        2500,
        [1200, 1200, 1200, 2000],
        [15000, 11000, 17000, 25000],
    )
)
