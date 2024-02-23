# Exercise programs

- [Exercise programs](#exercise-programs)
  - [Factorial](#factorial)
  - [Fibonacci Series](#fibonacci-series)
  - [Prime numbers](#prime-numbers)
  - [Armstrong numbers](#armstrong-numbers)
  - [Sum of Digits of a number](#sum-of-digits-of-a-number)
  - [Leetcode two sum problem](#leetcode-two-sum-problem)

**Conversion:**

- [Binary to Decimal](./conversions/binary_to_decimal.py)
- [Decimal to Binary](./conversions/decimal_to_binary.py)

## Factorial

Multiply a number by its descendants until 1.

**Example:**

$5*4*3*2*1 = 120$

## Fibonacci Series

Number Series starting from 0 adding the last value to the next value. [Python Code](./fibonacci_series.py)

**Example:**

$0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89$

## Prime numbers

Prime numbers are numbers that cannot be divided other than 1 or by the number itself. [Python Code](./prime_number.py)

**Example:**

$(5, 7,11,17,19)$

## Armstrong numbers

Armstrong is a number which is equal to the sum of its digits own digits raised to the power of the number of digits. [Python Code](./armstrong_number.py)

**Example:**

$(153,371,407)$

**Calculation:**216 + 27 + 64 + 1 = 308

**For 3 digits:**

$$
153 - (1^3 + 5^3 + 3^3 = 1+ 125 + 27 =153)
$$

**For 4 digits:**

$$
1634 - ( 1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634)
$$

## Sum of Digits of a number

Sum of Digits of a number. [Python Code](./sum_of_digits_of_num.py)

**Example:**
$$
(123 = 6)
(145 = 10)
$$

## Leetcode two sum problem

<https://leetcode.com/problems/two-sum/description/>

```yml
- Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

- You may assume that each input would have exactly one solution, and you may not use the same element twice.

- You can return the answer in any order.

Example:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

[Python Solution](./two_sum.py)
