from typing import List, Dict, Optional
from decimal import Decimal

from .constants import ISA_ANNUAL_ALLOWANCE, LISA_ANNUAL_ALLOWANCE

from ..schema.isa_allowance import (
    Account, IsaAllowance, Transaction, AccountType
)

IsaLimitMapping = Dict[AccountType, Decimal]

def calculate_isa_allowance_for_account(
    account: Account,
    transactions: List[Transaction],
    tax_year: int = 2024,
    annual_allowance_override: Optional[IsaLimitMapping] = None
) -> IsaAllowance:
    """
    Main entrypoint for calculating the ISA allowance for a given account.
    """
    limits = annual_allowance_override or get_isa_limits_for_tax_year(tax_year)
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
            AccountType.Flexible_ISA: ISA_ANNUAL_ALLOWANCE,
            AccountType.ISA: ISA_ANNUAL_ALLOWANCE,
            AccountType.Flexible_Lifetime_ISA: LISA_ANNUAL_ALLOWANCE,
        }
    else:
        raise NotImplementedError(f"ISA limits not defined for the tax year: {tax_year}")
