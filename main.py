def print_rec(a, b):
    try:
        for i in range(0, a):
            for j in range(0, b):
                print('*', end=" ")
            print()
        print()
    except Exception as ex:
     print(f"Error information")

print_rec(2, 15)