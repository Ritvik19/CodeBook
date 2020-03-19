def fibonacci(n):
    phi = (1 + 5**0.5) / 2
    return round(phi**n / 5**0.5)


if __name__ == "__main__":
    print("Using formula")
    print(fibonacci(9))
