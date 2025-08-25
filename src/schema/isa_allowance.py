import enum
from decimal import Decimal
from typing import List, Set

from pydantic import BaseModel, Field
import datetime as dt


class AccountType(enum.Enum):
    Non_Flexible_ISA = enum.auto()  # non-flexible
    Flexible_ISA = enum.auto()
    Flexible_Lifetime_ISA = enum.auto()

    @classmethod
    def get_isa_account_types(cls) -> Set["AccountType"]:
        return {cls.Flexible_ISA, cls.Flexible_Lifetime_ISA, cls.Non_Flexible_ISA}
        

class Transaction(BaseModel):
    transaction_date: dt.date
    amount: Decimal

class Client(BaseModel):
    id: int
    accounts: List['Account'] = Field(default_factory=list)

class Account(BaseModel):
    id: int
    account_type: AccountType
    transactions: List[Transaction] = Field(default_factory=list)

class TotalLimit(BaseModel):
    tax_year: str
    total_limit: Decimal

class IsaAllowance(BaseModel):
    annual_allowance: Decimal
    remaining_allowance: Decimal
