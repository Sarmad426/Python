"""
Currency Convertor
"""

from typing import Literal

CURRENCIES: tuple[str, str, str] = ("PKR", "USD", "IND")

TypeCurrency = Literal["Source", "Target"]

EXCHANGE_RATES: dict[str, dict[str, float]] = {
    "USD": {"PKR": 0.288, "IND": 0.48},
    "PKR": {"USD": 2.88, "IND": 1.48},
    "IND": {"PKR": 0.8, "USD": 0.2},
}


def get_amount() -> float:
    """
    Gets the amount from user, validates it and then returns it
    """
    while True:
        try:
            amount = input("Enter amount: ")
            if float(amount) <= 0:
                raise ValueError()
            return float(amount)
        except ValueError:
            print("Invalid amount! ")


def get_currency(label: TypeCurrency) -> str:
    """
    Gets the currency from user, validates it and then returns it
    """
    while True:

        currency = input(f"{label} currency (USD/PKR/IND): ").upper()
        if currency not in CURRENCIES:
            print("Invalid currency!")
        else:
            return currency


def convert(amount: float, source: str, target: str) -> float:
    """
    Converts source currency amount to target currency amount
    """
    if source == target:
        return amount

    return amount * EXCHANGE_RATES[source][target]


def main():
    """
    Main function
    """
    amount = get_amount()
    source_currency = get_currency("Source")
    target_currency = get_currency("Target")

    conversion = convert(amount, source_currency, target_currency)

    print(f"{source_currency} {amount} = {target_currency} {conversion}")


if __name__ == "__main__":
    main()
