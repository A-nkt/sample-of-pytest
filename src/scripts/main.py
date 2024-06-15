

def f(x: int):
    if x < 0:
        return None
    return x** 2 + 2*x + 1


if __name__ == '__main__':
    result = f(4)
    print(f'resut is {result}')