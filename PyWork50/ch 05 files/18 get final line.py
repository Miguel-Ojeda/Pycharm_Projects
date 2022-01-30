file_name = 'files/43-0.txt'


def get_final_line_v1(file_name):
    with open(file_name, encoding='UTF-8') as file:
        lineas = file.readlines()
    return lineas[-1]


def get_final_line_v2(file_name):
    with open(file_name, encoding='UTF-8') as file:
        for linea in file:
            linea_final = linea
    return linea_final


def get_final_line_v3(file_name):
    with open(file_name, encoding='UTF-8') as file:
        while True:
            linea = next(file, None)
            if linea:
                last_linea = linea
            else:
                break
    return last_linea


print(get_final_line_v1(file_name))
print(get_final_line_v2(file_name))
print(get_final_line_v3(file_name))


