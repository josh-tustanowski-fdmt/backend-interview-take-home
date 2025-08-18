# Engineering @Fundment - Take Home

Welcome to the Fundment take-home exercise for a backend developer
position! This exercise is designed to see how you can translate 
problem statements into working software and the design choices you
take to get there and make your software maintainable and extensible.

## The Task

Implement a stateless calculator that can determine the remaining allowance
for your ISA (Individual Savings Account).

## Implementation Steps

Complete the following steps in order, building upon each previous implementation:

### Step 1: Simple ISA (Non-Flexible)
Implement the calculator for a simple ISA (non-flexible) to get the remaining ISA allowance.

- **Key Rules**: 
  - Annual limit: £20,000 (2024/25 tax year)
  - Once withdrawn, contribution allowance is lost permanently
  - Calculate remaining allowance based on total contributions in tax year

### Step 2: Simple ISA (Flexible)
Implement the calculator for a simple ISA (flexible) to get the remaining ISA allowance.

- **Key Rules**:
  - Annual limit: £20,000 (2024/25 tax year)  
  - Withdrawals restore contribution allowance (can re-contribute withdrawn amounts)
  - Track net contributions vs. allowable contributions including restored amounts

### Step 3: Multiple ISA Accounts (Mixed Flexibility)
Consider the case of a client who has two ISA accounts, one flexible and the other non-flexible - how does the overall ISA allowance get impacted?

- **Key Rules**:
  - Combined ISA limit of £20,000 applies across all ISA accounts
  - Flexible account withdrawals can restore allowance for either account
  - Non-flexible account withdrawals permanently reduce total allowance

### Step 4: Lifetime ISA (Flexible)
Implement the calculator for a Lifetime ISA (flexible).

- **Key Rules**:
  - Annual limit: £4,000 (2024/25 tax year)
  - Separate allowance from regular ISA allowance
  - Withdrawals restore contribution allowance (flexible behavior)

### Step 5: Combined ISA and Lifetime ISA
Implement the calculator for the case of a client with an ISA and Lifetime ISA (the ISA limit is adjusted from the contributions from other ISAs in the accounts).

- **Key Rules**:
  - Lifetime ISA contributions count towards the overall £20,000 ISA allowance
  - Client has separate £4,000 Lifetime ISA allowance AND reduced regular ISA allowance
  - If £4,000 contributed to Lifetime ISA, only £16,000 remains for regular ISAs
  - Design considerations for cross-account allowance calculations

### Step 6: Custom ISA Limits (Inheritance)
Implement injecting custom ISA limits for your particular account - how does that impact your design? (This can happen with ISAs being inherited)

- **Key Rules**:
  - Inherited ISAs may have different annual allowance rules
  - Custom limits should be configurable per account or client
  - Consider how custom limits interact with standard limits
  - Design for extensibility to support various edge cases

## Getting Started

1. Review the existing code structure in `src/schema/isa_allowance.py` for data models
2. Implement your solution in `src/service/isa_allowance.py` 
3. The `calculate_isa_allowance_for_account()` function is your main entry point
4. Add comprehensive tests in the `tests/` directory
5. Consider edge cases and error handling throughout your implementation

## Design Considerations

- How will you handle the progression from simple to complex scenarios?
- What abstractions will make your code maintainable as requirements evolve?
