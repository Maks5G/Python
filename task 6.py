def check(num):
    i = 2
    while i < num:
        if num % i == 0:
            return False
        else:
            i += 1
    return True

def nextPrime(n):
    if check(n+1):
        return n+1
    else:
        return nextPrime(n+1)

number = int(input("Уведіть число: "))

result = nextPrime(number)
print("Перше просте число, яке більше за введене: ", result)
