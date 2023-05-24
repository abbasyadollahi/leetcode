import datetime
import unittest
from solution import monthly_charge

users = [
    {
        'id': 1,
        'name': 'Employee #1',
        'activated_on': datetime.date(2019, 1, 1),
        'deactivated_on': None,
        'customer_id': 1,
    },
    {
        'id': 2,
        'name': 'Employee #2',
        'activated_on': datetime.date(2019, 1, 1),
        'deactivated_on': None,
        'customer_id': 1,
    },
    {
        'id': 3,
        'name': 'Employee #3',
        'activated_on': datetime.date(2021, 12, 10),
        'deactivated_on': None,
        'customer_id': 1,
    },
    {
        'id': 4,
        'name': 'Employee #4',
        'activated_on': datetime.date(2021, 11, 30),
        'deactivated_on': datetime.date(2021, 12, 20),
        'customer_id': 1,
    },
    {
        'id': 5,
        'name': 'Employee #5',
        'activated_on': datetime.date(2022, 12, 15),
        'deactivated_on': datetime.date(2022, 12, 15),
        'customer_id': 1,
    },
]

plan = {
    'id': 1,
    'customer_id': 1,
    'monthly_price_in_cents': 5_000
}

no_users = []


class Test(unittest.TestCase):
    def test_works_when_no_users_are_active(self):
        self.assertEqual(monthly_charge('2018-10', plan, users), 0)

    def test_works_when_the_active_users_are_active_the_entire_month(self):
        expected_bill = 0
        expected_bill += 2 * 5_000
        self.assertAlmostEqual(monthly_charge('2020-12', plan, users), expected_bill, delta=1)

    def test_works_when_the_active_users_are_active_partial_month(self):
        expected_bill = 0
        expected_bill += 2 * 5_000
        expected_bill += ((1 + 31 - 10) / 31) * 5_000
        expected_bill += ((31 - (31 - 20)) / 31) * 5_000
        self.assertAlmostEqual(monthly_charge('2021-12', plan, users), expected_bill, delta=1)

    def test_works_when_the_active_users_are_active_one_day(self):
        expected_bill = 0
        expected_bill += 3 * 5_000
        expected_bill += (1 / 31) * 5_000
        self.assertAlmostEqual(monthly_charge('2022-12', plan, users), expected_bill, delta=1)
