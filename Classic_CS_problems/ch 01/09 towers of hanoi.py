from typing import TypeVar, Generic, List
T = TypeVar('T')
import cProfile


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)


num_discs: int = 20
tower_a: Stack[int] = Stack()
tower_b: Stack[int] = Stack()
tower_c: Stack[int] = Stack()
for i in range(1, num_discs + 1):
    tower_a.push(i)


def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int) -> None:
    if n == 1:
        end.push(begin.pop())
    else:
        hanoi(begin, temp, end, n - 1)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, n - 1)

if __name__ == "__main__":

    # hanoi(tower_a, tower_c, tower_b, num_discs)
    cProfile.run('hanoi(tower_a, tower_c, tower_b, num_discs)')
    '''
             5767165 function calls (4194304 primitive calls) in 2.257 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  1048575    0.357    0.000    0.485    0.000 09 towers of hanoi.py:10(push)
  1048575    0.335    0.000    0.479    0.000 09 towers of hanoi.py:13(pop)
1572862/1    1.293    0.000    2.257    2.257 09 towers of hanoi.py:28(hanoi)
        1    0.000    0.000    2.257    2.257 <string>:1(<module>)
        1    0.000    0.000    2.257    2.257 {built-in method builtins.exec}
  1048575    0.127    0.000    0.127    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  1048575    0.143    0.000    0.143    0.000 {method 'pop' of 'list' objects}
    '''
