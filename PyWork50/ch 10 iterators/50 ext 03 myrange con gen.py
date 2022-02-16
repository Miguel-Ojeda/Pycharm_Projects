"""
In the “Beyond the exercise” section for exercise 47 ext 03, you implemented a MyRange class,
which mimics the built-in range class.

Now do the same thing, but using a generator expression.
"""

def my_range(first, second=None, step=1):
    if second is None:
        index = 0
        limit = first
    else:
        index = first
        limit = second

    while index < limit:
        yield index
        index += step


for i in my_range(2, 10, 3):
    print(i)