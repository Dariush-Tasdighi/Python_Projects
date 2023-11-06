"""Project 100"""


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


if luhn_checksum("4532015112830366") == 0:
    print("Valid")
else:
    print("Invalid")
