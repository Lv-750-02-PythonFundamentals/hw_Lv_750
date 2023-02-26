def convert_to_float(int_lst: list[int]):
    return [float(i) for i in int_lst]


def fibonacci(number):
    fib1 = fib2 = 1
    fib_lst = []
    if number == 1:
        fib_lst.append(fib1)
        return fib_lst
    if number == 2:
        fib_lst.append(fib1)
        fib_lst.append(fib2)
        return fib_lst
    fib_lst.append(fib1)
    fib_lst.append(fib2)
    for i in range(2, number):
        fib1, fib2 = fib2, fib1 + fib2
        fib_lst.append(fib2)
    return fib_lst


if __name__ == "__main__":
    print(convert_to_float([1, 2, 3, 4, 5]))
    print(*fibonacci(12))
