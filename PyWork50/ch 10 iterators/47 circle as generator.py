# Implement Circle as a generator function, rather than as a class.

def circle(secuencia, max_times):
    index = 0
    while index < max_times:
        yield secuencia[index % len(secuencia)]
        index += 1

def circle_2(secuencia, max_times):
    for index in range(max_times):
        yield secuencia[index % len(secuencia)]


if __name__ == '__main__':
    # Pruebas....
    c = circle('abcde', 17)
    for i in c:
        print(i)

    print('---------------')
    print(list(circle('1x2', 14)))

