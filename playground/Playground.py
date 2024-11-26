import re


def main() -> bool:
    rics = ["ABCU5", "ABCU56", "JPYUSD="]
    pattern = re.compile(r"(?P<other>[A-Z]\d{1,2})?$")
    for ric in rics:
        match = pattern.search(ric)
        print(ric, match.groups())


main()
