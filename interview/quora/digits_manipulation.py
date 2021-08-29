def digitsManipulation(n: int) -> int:
    digits = []
    while n:
        digits.append(n % 10)
        n //= 10

    product = 1
    for digit in digits:
        product *= digit

    return product - sum(digits)
