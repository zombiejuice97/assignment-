import square

def cube(num):
    cub = square.square(num) * num
    return cub

print(cube(2))