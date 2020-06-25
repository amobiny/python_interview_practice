# Multiplying two numbers using recursion and Karatsuba's method
# https://en.m.wikipedia.org/wiki/Karatsuba_algorithm#Pseudocode


def split_at(num, n):
    """
    splits num from after its n digit from the right side
    :param num: integer number to be splitted
    :param n: split digit index
    :return: high and low part of the num after split
    """
    return num / 10**n, num % 10**n


def mult(num1, num2):
    if num1 < 10 or num2 < 10:
        return num1 * num2
    else:
        # split the bigger number
        m = max(len(str(num1)), len(str(num2)))
        m2 = m / 2
        high1, low1 = split_at(num1, m2)
        high2, low2 = split_at(num2, m2)
        z0 = mult(low1, low2)
        z1 = mult((low1 + high1), (low2 + high2))
        z2 = mult(high1, high2)

    return (z2 * 10**(2*m2)) + ((z1 - z2 - z0) * 10**m2) + z0


print(mult(34276, 4234))
print()

