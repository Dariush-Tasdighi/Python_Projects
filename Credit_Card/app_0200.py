"""Project 200"""


def luhn_checksum(card_number):
    """Luhn Checksum"""

    def digits_of(n):
        return [int(d) for d in str(n)]

    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    return checksum % 10


SUFFIX = "1234"
PREFIX = "543210"
MAIN_NUMBER = 123_457
# MAIN_NUMBER = 123457

# 543210******1234
# 543210[100_000]1234
# 543210[999_999]1234

for number in range(100_000, 1_000_000):
    credit_card = f"{PREFIX}{number}{SUFFIX}"
    credit_card_number = int(credit_card)
    if credit_card_number % MAIN_NUMBER == 0:
        if luhn_checksum(credit_card) == 0:
            print(credit_card)
            break

# 5432103279251234
# CTFlearn{card_number}
# Solution: CTFlearn{5432103279251234}
