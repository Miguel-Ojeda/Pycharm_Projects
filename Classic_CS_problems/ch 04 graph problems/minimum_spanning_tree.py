"""
Cómo calcular el minimum spanning tree de un weighted graph??
Algoritmo de Jarnik (también llamado Primm's algorithm)

Jarník’s algorithm for finding a minimum spanning tree works by dividing a graph
into two parts:
* the vertices in the still-being-assembled minimum spanning tree and
** the vertices not yet in the minimum spanning tree.

It takes the following steps:
1 Pick an arbitrary vertex to include in the minimum spanning tree.
2 Find the lowest-weight edge connecting the minimum spanning tree to the vertices
not yet in the minimum spanning tree.
3 Add the vertex at the end of that minimum edge to the minimum spanning tree.
4 Repeat steps 2 and 3 until every vertex in the graph is in the minimum spanning tree.
"""

from typing import TypeVar, List, Optional
from weighted_graph import WeightedGraph
from weighted_edge import WeightedEdge
from priority_queue import PriorityQueue

V = TypeVar('V') # type of the vertices in the graph
WeightedPath = List[WeightedEdge] # type alias for paths

# función auxiliar
def total_weight(wp: WeightedPath) -> float:
    return sum(edge.weight for edge in wp)

def mst(wg: WeightedGraph[V], start: int = 0) -> Optional[WeightedPath]:
    """
    start nos indica en qué vértice queremos empezar como
    inicio del algoritmo de Jarnik.... en principio sería indiferente, el
    resultado debería ser siempre el mismo...
    """
    # if not (0 <= start < wg.vertex_count):
    if start > (wg.vertex_count - 1) or start < 0:
        return None
    result: WeightedPath = []  # holds the final MS
    pq: PriorityQueue[WeightedEdge] = PriorityQueue()
    visited: [bool] = [False] * wg.vertex_count
    # o sea, es una lista donde cada item nos indica si ya ese vértice lo hemos visitado!!!!

    def visit(index: int):
        visited[index] = True
        for an_edge in wg.edges_for_index(index):
            if not visited[an_edge.v]:
                pq.push(an_edge)

    visit(start)

    while not pq.empty:
        edge = pq.pop()
        if visited[edge.v]:
            continue  # ya lo habíamos visitado, no hay nada que hacer
        result.append(edge)
        visit(edge.v)

    return result


def print_weighted_path(wg: WeightedGraph, wp: WeightedPath) -> None:
    for edge in wp:
        print(f"{wg.vertex_at(edge.u)} ({edge.weight}) -> {wg.vertex_at(edge.v)}")
    print(f"Total Weight: {total_weight(wp)}")


if __name__ == "__main__":
    city_graph2: WeightedGraph[str] = WeightedGraph(["Seattle", "San Francisco", "Los Angeles",
                                                     "Riverside", "Phoenix", "Chicago", "Boston",
                                                     "New York", "Atlanta", "Miami", "Dallas", "Houston",
                                                     "Detroit", "Philadelphia", "Washington"])
    city_graph2.add_edge_by_vertices("Seattle", "Chicago", 1737)
    city_graph2.add_edge_by_vertices("Seattle", "San Francisco", 678)
    city_graph2.add_edge_by_vertices("San Francisco", "Riverside", 386)
    city_graph2.add_edge_by_vertices("San Francisco", "Los Angeles", 348)
    city_graph2.add_edge_by_vertices("Los Angeles", "Riverside", 50)
    city_graph2.add_edge_by_vertices("Los Angeles", "Phoenix", 357)
    city_graph2.add_edge_by_vertices("Riverside", "Phoenix", 307)
    city_graph2.add_edge_by_vertices("Riverside", "Chicago", 1704)
    city_graph2.add_edge_by_vertices("Phoenix", "Dallas", 887)
    city_graph2.add_edge_by_vertices("Phoenix", "Houston", 1015)
    city_graph2.add_edge_by_vertices("Dallas", "Chicago", 805)
    city_graph2.add_edge_by_vertices("Dallas", "Atlanta", 721)
    city_graph2.add_edge_by_vertices("Dallas", "Houston", 225)
    city_graph2.add_edge_by_vertices("Houston", "Atlanta", 702)
    city_graph2.add_edge_by_vertices("Houston", "Miami", 968)
    city_graph2.add_edge_by_vertices("Atlanta", "Chicago", 588)
    city_graph2.add_edge_by_vertices("Atlanta", "Washington", 543)
    city_graph2.add_edge_by_vertices("Atlanta", "Miami", 604)
    city_graph2.add_edge_by_vertices("Miami", "Washington", 923)
    city_graph2.add_edge_by_vertices("Chicago", "Detroit", 238)
    city_graph2.add_edge_by_vertices("Detroit", "Boston", 613)
    city_graph2.add_edge_by_vertices("Detroit", "Washington", 396)
    city_graph2.add_edge_by_vertices("Detroit", "New York", 482)
    city_graph2.add_edge_by_vertices("Boston", "New York", 190)
    city_graph2.add_edge_by_vertices("New York", "Philadelphia", 81)
    city_graph2.add_edge_by_vertices("Philadelphia", "Washington", 123)

    result: Optional[WeightedPath] = mst(city_graph2)

    if result is None:
        print("No solution found!")
    else:
        print_weighted_path(city_graph2, result)

