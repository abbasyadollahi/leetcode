# https://www.hackerrank.com/x/library/hackerrank/all/questions/433457/view

from typing import List, Tuple


def getUnallottedUsers(bids: List[Tuple[int, int, int, int]], totalShares: int) -> List[int]:
    UID, SHARES, PRICE, TIME = range(4)

    bids.sort(reverse=True, key=lambda bid: [bid[PRICE], -bid[TIME]])

    shares_by_uid_by_price = {}
    for bid in bids:
        uid = bid[UID]
        shares = bid[SHARES]
        price = bid[PRICE]
        if price in shares_by_uid_by_price:
            shares_by_uid_by_price[price][uid] = shares
        else:
            shares_by_uid_by_price[price] = {uid: shares}

    all_unallotted = []
    for shares_by_uid in shares_by_uid_by_price.values():
        unallotted = set(shares_by_uid.keys())
        while shares_by_uid and totalShares > 0:
            allotted = set()
            for uid, shares in shares_by_uid.items():
                if shares == 0:
                    allotted.add(uid)
                elif totalShares > 0:
                    shares_by_uid[uid] -= 1
                    totalShares -= 1
                    unallotted.discard(uid)
                elif totalShares == 0:
                    break

            for uid in allotted:
                del shares_by_uid[uid]
        all_unallotted.extend(unallotted)

    return sorted(all_unallotted)
