# Super conciso
# Usa Sets Comprehensions!!!

def different_ips(filename):
    return {one_line.split()[0] for one_line in open(filename)}


def different_responses(filename):
    return {one_line.split()[8] for one_line in open(filename)}

# Ufff, supercompacto... quizás es más confuso, pero no mucho, la verdad...
