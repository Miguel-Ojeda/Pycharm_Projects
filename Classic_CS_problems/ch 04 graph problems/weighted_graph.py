from graph import Graph
from weighted_edge import WeightedEdge
from typing import List, TypeVar, Generic, Optional, Tuple

V = TypeVar('V')


class WeightedGraph(Generic[V], Graph[V]):
    def __init__(self, vertices: Optional[List[V]] = None) -> None:
        if vertices is None:
            vertices = []
        self._vertices = vertices
        self._edges: List[List[WeightedEdge]] = [[] for _ in vertices]
        # igual no habría que poner esta función, ya que realmente hace lo mismo
        # excepto con los edges son de tipos distintos, aquí con peso, pero como
        # es una lista vacía inicialmente no sé si serviría ...

    # Habrá que reescribir todas las cosas que añaden edges, ya que ahora tb hay peso
    def add_edge_by_indices(self, u: int, v: int, weight: float) -> None:
        edge: WeightedEdge = WeightedEdge(u, v, weight)
        self.add_edge(edge)  # llamamos la función de la clase base

    def add_edge_by_vertices(self, first: V, second: V, weight: float) -> None:
        first_index = self.index_of(first)
        second_index = self.index_of(second)
        self.add_edge_by_indices(first_index, second_index, weight)

    def neighbors_for_index_with_weights(self, index: int) -> List[Tuple[V, float]]:
        """
        Nos retorna una lista de tuplas, donde cada tupla es
        un vértice y el costo de llegar hasta ese vértice
        """
        distance_tuples: List[Tuple[V, float]] = []
        edge: WeightedEdge
        for edge in self.edges_for_index(index):
            distance_tuples.append((self.vertex_at(edge.v), edge.weight))
        return distance_tuples

    # Make it easy to pretty-print a Graph
    def __str__(self) -> str:
        desc: str = f'El total de vértices es {self.vertex_count}:\n'
        for i in range(self.vertex_count):
            desc += f"{self.vertex_at(i)} -> {self.neighbors_for_index_with_weights(i)}\n"
        desc += f'En total hay {self.edges_count} aristas\n'
        return desc


if __name__ == "__main__":
    # test basic Graph construction
    city_graph_2: WeightedGraph[str] = WeightedGraph(["Seattle", "San Francisco", "Los Angeles", "Riverside",
                                                      "Phoenix", "Chicago", "Boston", "New York", "Atlanta",
                                                      "Miami", "Dallas", "Houston", "Detroit", "Philadelphia",
                                                      "Washington"])
    city_graph_2.add_edge_by_vertices("Seattle", "Chicago", 1737)
    city_graph_2.add_edge_by_vertices("Seattle", "San Francisco", 678)
    city_graph_2.add_edge_by_vertices("San Francisco", "Riverside", 386)
    city_graph_2.add_edge_by_vertices("San Francisco", "Los Angeles", 348)
    city_graph_2.add_edge_by_vertices("Los Angeles", "Riverside", 50)
    city_graph_2.add_edge_by_vertices("Los Angeles", "Phoenix", 357)
    city_graph_2.add_edge_by_vertices("Riverside", "Phoenix", 307)
    city_graph_2.add_edge_by_vertices("Riverside", "Chicago", 1704)
    city_graph_2.add_edge_by_vertices("Phoenix", "Dallas", 887)
    city_graph_2.add_edge_by_vertices("Phoenix", "Houston", 1015)
    city_graph_2.add_edge_by_vertices("Dallas", "Chicago", 805)
    city_graph_2.add_edge_by_vertices("Dallas", "Atlanta", 721)
    city_graph_2.add_edge_by_vertices("Dallas", "Houston", 225)
    city_graph_2.add_edge_by_vertices("Houston", "Atlanta", 702)
    city_graph_2.add_edge_by_vertices("Houston", "Miami", 968)
    city_graph_2.add_edge_by_vertices("Atlanta", "Chicago", 588)
    city_graph_2.add_edge_by_vertices("Atlanta", "Washington", 543)
    city_graph_2.add_edge_by_vertices("Atlanta", "Miami", 604)
    city_graph_2.add_edge_by_vertices("Miami", "Washington", 923)
    city_graph_2.add_edge_by_vertices("Chicago", "Detroit", 238)
    city_graph_2.add_edge_by_vertices("Detroit", "Boston", 613)
    city_graph_2.add_edge_by_vertices("Detroit", "Washington", 396)
    city_graph_2.add_edge_by_vertices("Detroit", "New York", 482)
    city_graph_2.add_edge_by_vertices("Boston", "New York", 190)
    city_graph_2.add_edge_by_vertices("New York", "Philadelphia", 81)
    city_graph_2.add_edge_by_vertices("Philadelphia", "Washington", 123)
    print(city_graph_2)
