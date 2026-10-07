import os
import sys


def calculate_transfer(amount, commission):
    unused_value = 100
    total=amount+commission
    if amount > 0:
      return total
    else:
      return 0


def can_transfer(balance,amount):
    if amount > 0 and balance >= amount:
        return True
    else:
        return False


print(calculate_transfer(10000,100))
