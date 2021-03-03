def fibonacci_sum():
    #calculate the sum of the even-valued terms of Fibonacci sequence up to 4000000 exclued, starting from 1 and 2
    sum = 2
    a = 0
    b = 1
    c = 2

    #every iteration c assumes the value of the next member of the Fibonacci sequence
    while c < 4000000:
        a = b
        b = c
        c = c + a
        if c % 2 == 0:
            sum = sum + c

    return (sum)

if __name__=="__main__":
    print(fibonacci_sum())
