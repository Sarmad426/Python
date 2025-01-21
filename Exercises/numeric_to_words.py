def int_to_english(num):
    d = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
    }
    k = 1000
    m = k * 1000
    b = m * 1000

    if num < 0:
        raise ValueError("Only non-negative numbers are supported.")

    if num < 20:
        return d[num]
    elif num < 100:
        if num % 10 == 0:
            return d[num]
        else:
            return d[num // 10 * 10] + "-" + d[num % 10]
    elif num < k:
        if num % 100 == 0:
            return d[num // 100] + " hundred"
        else:
            return d[num // 100] + " hundred and " + int_to_english(num % 100)
    elif num < m:
        if num % k == 0:
            return int_to_english(num // k) + " thousand"
        else:
            return int_to_english(num // k) + " thousand, " + int_to_english(num % k)
    elif num < b:
        if num % m == 0:
            return int_to_english(num // m) + " million"
        else:
            return int_to_english(num // m) + " million, " + int_to_english(num % m)
    else:
        if num % b == 0:
            return int_to_english(num // b) + " billion"
        else:
            return int_to_english(num // b) + " billion, " + int_to_english(num % b)


def main():
    try:
        num = int(input("Enter a non-negative integer: "))
        if num < 0:
            print("Negative numbers are not supported.")
        else:
            print(int_to_english(num))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
