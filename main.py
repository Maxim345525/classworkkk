def is_prime(a):
    if a % a == 0 and a != 0:
        return True
    else:
        return False
a = int(input("Enter a number: "))
print(is_prime(a))
