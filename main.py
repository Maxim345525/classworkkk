def get_cube_root(x):
    if x < 0:
        x = abs(x)
        cube_root = x**(1/3)*(-1)
    else:
        cube_root = x**(1/3)
    return cube_root

print(round(get_cube_root(64)))
print(get_cube_root(-64))