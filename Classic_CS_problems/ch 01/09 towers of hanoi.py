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


num_discs: int = 3
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
     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        7    0.000    0.000    0.000    0.000 09 towers of hanoi.py:10(push)
        7    0.000    0.000    0.000    0.000 09 towers of hanoi.py:13(pop)
     10/1    0.000    0.000    0.000    0.000 09 towers of hanoi.py:28(hanoi)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        7    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        7    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
    '''
    print(tower_a)
    print(tower_b)
    print(tower_c)


    '''Esto no mola, sube demasiado...
    num_discs = 20!!
       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  1048575    0.280    0.000    0.389    0.000 09 towers of hanoi.py:10(push)
  1048575    0.282    0.000    0.413    0.000 09 towers of hanoi.py:13(pop)
1572862/1    0.995    0.000    1.797    1.797 09 towers of hanoi.py:28(hanoi)
        1    0.000    0.000    1.797    1.797 <string>:1(<module>)
        1    0.000    0.000    1.797    1.797 {built-in method builtins.exec}
  1048575    0.108    0.000    0.108    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  1048575    0.131    0.000    0.131    0.000 {method 'pop' of 'list' objects}
  '''