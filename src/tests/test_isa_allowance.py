import datetime as dt
from decimal import Decimal
from unittest import TestCase

from ..schema.isa_allowance import Account, AccountType, Client, Transaction
from ..service.constants import ISA_ANNUAL_ALLOWANCE
from ..service.isa_allowance import calculate_isa_allowance_for_account


class TestIsaAllowanceCalculatorStep1(TestCase):
    def test_simple_non_flexible_isa_allowance_calculator(self) -> None:
        client = Client(id=1)
        account = Account(
            id=1,
            account_type=AccountType.Non_Flexible_ISA,
            transactions=[
                Transaction(
                    amount=Decimal(5_000), transaction_date=dt.date(2024, 5, 10)
                ),
                Transaction(
                    amount=Decimal(10_000), transaction_date=dt.date(2024, 5, 10)
                ),
            ],
        )
        client.accounts.append(account)
        allowance = calculate_isa_allowance_for_account(
            client=client, account=account, tax_year=2024
        )
        assert allowance.annual_allowance == Decimal(20_000)
        assert allowance.remaining_allowance == Decimal(5_000)

    def test_simple_non_flexible_isa_allowance_calculator_with_withdrawal(self) -> None:
        client = Client(id=1)
        account = Account(
            id=1,
            account_type=AccountType.Non_Flexible_ISA,
            transactions=[
                Transaction(
                    amount=Decimal(5_000), transaction_date=dt.date(2024, 5, 10)
                ),
                Transaction(
                    amount=Decimal(10_000), transaction_date=dt.date(2024, 5, 10)
                ),
                Transaction(
                    amount=Decimal(-10_000), transaction_date=dt.date(2024, 6, 10)
                ),
            ],
        )
        client.accounts.append(account)
        allowance = calculate_isa_allowance_for_account(
            client=client, account=account, tax_year=2024
        )
        assert allowance.annual_allowance == Decimal(20_000)
        assert allowance.remaining_allowance == Decimal(5_000)


class TestIsaAllowanceCalculatorStep5(TestCase):
    def test_combined_isa_and_lisa_with_large_isa_contributions(self) -> None:
        """
        Example Case - Showing how the contributions feed into each other.

        * The 20k ISA allowance is shared across the ISA and LISA account under a client
        * If we contribute more than 16k into an ISA, then the LISA annual limit is decreased by the contributions over 16k
           into the ISA
        * Example below:
            * 17k ISA contribution. Leaving 3k to contribute across the ISA and LISA.
            * The original 4k annual limit now is not valid, since a 4k contribution would take us over the total 20k figure.
            * The LISA remaining limit
        """
        client = Client(id=1)
        isa_account = Account(
            id=1,
            account_type=AccountType.Flexible_ISA,
            transactions=[
                Transaction(
                    amount=Decimal(17_000), transaction_date=dt.date(2024, 5, 10)
                )
            ],
        )
        lisa_account = Account(
            id=2, account_type=AccountType.Flexible_Lifetime_ISA, transactions=[]
        )
        client.accounts.extend([isa_account, lisa_account])

        lisa_allowance = calculate_isa_allowance_for_account(
            client=client, account=lisa_account, tax_year=2024
        )
        assert lisa_allowance.remaining_allowance == Decimal(3_000)
        assert lisa_allowance.annual_allowance == Decimal(3_000)

        isa_allowance = calculate_isa_allowance_for_account(
            client=client, account=isa_account, tax_year=2024
        )
        assert isa_allowance.remaining_allowance == Decimal(3_000)
        assert isa_allowance.annual_allowance == ISA_ANNUAL_ALLOWANCE


class TestIsaAllowanceCalculatorStep6(TestCase):
    def test_adjust_isa_annual_allowance_from_inheritance(self) -> None:
        """
        Example Case - Adjusting the ISA annual allowance. This can happen for a few exception cases,
        the most common is inheriting an ISA - this effectively acts as additional permitted subscriptions to a
        tax year. In the industry this is known as an "APS Transfer".

        * APS Transfer into an ISA of 40k
        """
        pass
