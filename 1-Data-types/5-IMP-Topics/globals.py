"""
    Python code explains global variables

    - `account` function to `deposit` and `withdraw` money
    - `deposit` and `withdraw` functions to deposit and withdraw money
"""

balance: int = 0


def account():
    """
    `deposit` and `withdraw` money

    No Parameters: \n
    Returns Nothing.
    """
    print(f"Balance: {balance}")
    deposit(100)
    print(f"Balance after deposit: {balance}")
    withdraw(50)
    print(f"Balance after Withdraw: {balance}")


def deposit(amount: int) -> None:
    """
    Deposit Money

    Parameters:
    - amount (int) : Deposit the money via using `global balance` variable

    Returns Nothing.
    """
    global balance
    balance += amount


def withdraw(amount: int) -> None:
    """
    Withdraw Money

    Parameters:
    - amount (int) : Withdraw the money via using `global balance` variable

    Returns Nothing.
    """
    global balance
    balance -= amount


if __name__ == "__main__":
    account()


# var = 1


# def foo():
#     global var  # [global-statement]
#     var = 10
#     print(var)


# foo()
# print(var)
