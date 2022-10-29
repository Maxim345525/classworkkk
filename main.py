dev(maximum(a, b))
    if a>b:
        print("a")
    elif a<b:
        print("b")

a = int(input("Введіть число->"))
b = int(input("Введіть число->"))
print(maximum(a, b))