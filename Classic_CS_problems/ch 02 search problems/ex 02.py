"""Add a counter to dfs(), bfs(), and astar() to see how many states each
searches through for the same maze. Find the counts for 100 different mazes to
get statistically significant results
"""


from generic_search import bfs, dfs, astar, node_to_path
from laberinto_search import Maze, manhattan_distance
from statistics import mean


NUMERO_TEST = 100
resultados = {'DFS estados recorridos': [], 'DFS pasos solucion': [],
              'BFS estados recorridos': [], 'BFS pasos solucion': [],
              'A* estados recorridos': [], 'A* pasos solucion': []}


for test in range(NUMERO_TEST):
    print('Test --> laberinto', test)
    laberinto = Maze(rows=40, columns=40, sparseness=.26)

    estados_recorridos, solution_1 = dfs(laberinto.start, laberinto.goal_test, laberinto.successors)
    if solution_1 is None:
        continue
    path = node_to_path(solution_1)
    resultados['DFS estados recorridos'].append(estados_recorridos)
    resultados['DFS pasos solucion'].append(len(path))

    estados_recorridos, solution_1 = bfs(laberinto.start, laberinto.goal_test, laberinto.successors)
    if solution_1 is None:
        continue
    path = node_to_path(solution_1)
    resultados['BFS estados recorridos'].append(estados_recorridos)
    resultados['BFS pasos solucion'].append(len(path))

    heuristica = manhattan_distance(laberinto.goal)
    estados_recorridos, solution_1 = astar(laberinto.start, laberinto.goal_test, laberinto.successors, heuristica)
    if solution_1 is None:
        continue
    path = node_to_path(solution_1)
    resultados['A* estados recorridos'].append(estados_recorridos)
    resultados['A* pasos solucion'].append(len(path))

print('RESULTADOS')
print('DFS Media estados recorridos', mean(resultados['DFS estados recorridos']))
print('DFS Media pasos solución', mean(resultados['DFS pasos solucion']))
print('BFS Media estados recorridos', mean(resultados['BFS estados recorridos']))
print('BFS Media pasos solución', mean(resultados['BFS pasos solucion']))
print('A* Media estados recorridos', mean(resultados['A* estados recorridos']))
print('A* Media pasos solución', mean(resultados['A* pasos solucion']))


'''RESULTADOS
DFS Media estados recorridos 680.3561643835617
DFS Media pasos solución 306.6986301369863
BFS Media estados recorridos 1165.6712328767123
BFS Media pasos solución 79.3013698630137
A* Media estados recorridos 411.54794520547944
A* Media pasos solución 79.3013698630137
'''

'''Observaciones:
    El algoritmo más lento es el BFS
    El más rápido es A*
    El DFS es intermedio

    El algoritmo DFS produce resultados no óptimos
    Tanto BFS como A* producen la solución óptima

    La diferencia es que A* es mucho más rápido
'''