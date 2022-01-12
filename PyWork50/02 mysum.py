# The challenge here is to write a mysum function that does the same thing as the
# built-in sum function. However, instead of taking a single sequence as a parameter, it
# should take a variable number of arguments. Thus, although you might invoke
# sum([1,2,3]), you’d instead invoke mysum(1,2,3) or mysum(10,20,30,40,50).

def mysum(*argv):
    total = 0
    for item in argv:
        total += item
    return total

print(mysum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(mysum(*[2, 3, 4, 5], *[6, 7, 6, 5], *(2, 3, 4, 5)))

print(mysum(* range(11)))
