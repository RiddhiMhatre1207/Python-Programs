def fibonacci_series(n):
    """Return the first n Fibonacci numbers."""
    if n <= 0:
        return []
    series = [0, 1]
    while len(series) < n:
        series.append(series[-1] + series[-2])
    return series[:n]


if __name__ == "__main__":
    n = int(input("Enter number of terms: "))
    print(fibonacci_series(n))