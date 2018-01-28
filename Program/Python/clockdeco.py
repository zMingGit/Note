from clockdeco import clock


@clock
def test(n):
    if n < 2:
        return n
    return test(n-2) + test(n-1)

if __name__ == '__main__':
    print test(10)
