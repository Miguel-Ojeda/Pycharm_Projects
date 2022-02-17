# Write a function, sum_numeric, that takes any number of arguments. If the
# argument is or can be turned into an integer, then it should be added to the
# total. Arguments that can’t be handled as integers should be ignored. The
# result is the sum of the numbers. Thus, sum_numeric(10, 20, 'a', '30',
# 'bcd') would return 60. Notice that even if the string 30 is an element in the
# list, it’s converted into an integer and added to the total.

def sum_numeric(*argv):
    suma = 0
    for item in argv:
        try:
            suma += int(item)
        except ValueError:
            pass
    return suma

print(sum_numeric(1, 2, 3, '4', 5.5, '7.2', 'aaa'))


