from typing import List, Dict, Optional, Set
from decimal import Decimal

from .constants import ISA_ANNUAL_ALLOWANCE, LISA_ANNUAL_ALLOWANCE

from ..schema.isa_allowance import (
    Account,
    IsaAllowance, 
    AccountType,
    Client,
    Transaction,
)

IsaLimitMapping = Dict[AccountType, Decimal]

def calculate_isa_allowance_for_account(
    client: Client,
    account: Account,
    tax_year: int = 2024,
    annual_allowance_override: Optional[IsaLimitMapping] = None
) -> IsaAllowance:
    """
    Main entrypoint for calculating the ISA allowance for a given account.
    The client object contains all accounts and their transactions.
    """
    limits = annual_allowance_override or get_isa_limits_for_tax_year(tax_year)
    client_transactions = get_client_transactions(client, account_types=AccountType.get_isa_account_types())
    # TODO: Put in place checks on the tax-year for each transaction.
    return IsaAllowance(
        annual_allowance=limits.get(account.account_type, Decimal("0")),
        remaining_allowance=Decimal("0")
    )


def get_client_transactions(
    client: Client, 
    account_types: Set[AccountType],
) -> List[Transaction]:
    accounts = [account for account in client.accounts if account.account_type in account_types]
    return [t for a in accounts for t in a.transactions]



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
        raise NotImplementedError(f"ISA limits not defined for the tax year: {tax_year}")
