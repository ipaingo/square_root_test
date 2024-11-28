import math


def get_square_roots(a, b, c):
    if a == 0 and b == 0 and c == 0:
        return "Бесконечность"
    if a == 0:
        return None if b == 0 else -c / b
    if b == 0:
        if c == 0:
            return 0
        elif c > 0:
            return None
        else:
            sqrt_c = math.sqrt(-c / a)
            return [-sqrt_c, sqrt_c]
    if c == 0:
        return [0, -b / a]

    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None
    elif discriminant == 0:
        return -b / (2 * a)
    else:
        sqrt_d = math.sqrt(discriminant)
        return [(-b - sqrt_d) / (2 * a), (-b + sqrt_d) / (2 * a)]


def main():
    print(get_square_roots(3, 6, 0))


if __name__ == "__main__":
    main()
