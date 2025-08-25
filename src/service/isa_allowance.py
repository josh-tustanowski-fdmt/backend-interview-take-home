from decimal import Decimal
from typing import Dict

from ..schema.isa_allowance import Account, AccountType, Client, IsaAllowance
from .constants import ISA_ANNUAL_ALLOWANCE, LISA_ANNUAL_ALLOWANCE

IsaLimitMapping = Dict[AccountType, Decimal]


def calculate_isa_allowance_for_account(
    client: Client,
    account: Account,
    tax_year: int = 2024,
) -> IsaAllowance:
    """
    Main entrypoint for calculating the ISA allowance for a given account.

    Points to note:
    * The client object contains all accounts and their transactions.
    * The contributions from other ISA accounts under a client can influence the ISA calculator
    """
    limits = get_isa_limits_for_tax_year(tax_year)
    return IsaAllowance(
        annual_allowance=limits.get(account.account_type, Decimal("0")),
        remaining_allowance=Decimal("0"),
    )


def get_isa_limits_for_tax_year(tax_year: int) -> IsaLimitMapping:
    """
    Get the ISA limits for different account types in a specific tax year.
    """
    if tax_year == 2024:
        return {
            AccountType.Flexible_ISA: ISA_ANNUAL_ALLOWANCE,
            AccountType.Non_Flexible_ISA: ISA_ANNUAL_ALLOWANCE,
            AccountType.Flexible_Lifetime_ISA: LISA_ANNUAL_ALLOWANCE,
        }
    else:
        raise NotImplementedError(
            f"ISA limits not defined for the tax year: {tax_year}"
        )
