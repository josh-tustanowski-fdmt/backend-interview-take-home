from typing import List, Dict
from decimal import Decimal

from ..schema.isa_allowance import (
    Account, IsaAllowance, Transaction, AccountType
)

IsaLimitMapping = Dict[AccountType, Decimal]

def calculate_isa_allowance_for_account(
    account: Account,
    transactions: List[Transaction],
    tax_year: int = 2024,
) -> IsaAllowance:
    """
    Main entrypoint for calculating the ISA allowance for a given account.
    """
    limits = get_isa_limits_for_tax_year(tax_year)
    return IsaAllowance(
        annual_allowance=limits.get(account.account_type, Decimal("0")),
        remaining_allowance=Decimal("0")
    )


def get_isa_limits_for_tax_year(tax_year: int) -> IsaLimitMapping:
    """
    Get the ISA limits for different account types in a specific tax year.
    """
    if tax_year == 2024:
        return {
            AccountType.Flexible_ISA: Decimal("20_000.00"),
            AccountType.ISA: Decimal("20_000.00"),
            AccountType.Flexible_Lifetime_ISA: Decimal("4_000.00")
        }
    else:
        raise NotImplementedError(f"ISA limits not defined for the tax year: {tax_year}")
