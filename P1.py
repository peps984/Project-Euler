def multiples():
    sum = 0
    for x in range(1000):
        if (x % 3 == 0) or (x % 5 == 0):
            sum = sum + x
    return (sum)

if __name__ == "__main__":
    print(multiples())
