from typing import TypeVar, Generic, List, Optional
from edge import Edge

V = TypeVar('V')


class Graph(Generic[V]):
    """ Los grafos van a estar formados por V (estructura genérica, adaptable)
    Cada V tb tendrá asociado un int, que va a indicar el índice en la lista de Vértices
    Habrá tb una lista, donde cada ítem es la lista de aristas del vértice con ese índice
    Recordemos que las aristas(edges) se identifican con enteros u (from) y v (to),
    """
    def __init__(self, vertices: Optional[List[V]] = None) -> None:
        if vertices is None:
            self._vertices = []
        self._vertices = vertices
        # Guardamos una lista, donde cada ítem es la lista de aristas de cada vértice
        # Así, el primer elemento va a ser la lista de aristas del primer vértice, etc.
        self._edges: List[List[Edge]] = [[] for _ in vertices]

    @property
    def vertex_count(self) -> int:
        return len(self._vertices)

    @property
    def edges_count(self) -> int:
        # Observar que, nos da el número de aristas, pero
        # la misma arista existe dos veces (la original y la invertida)
        return sum(map(len, self._edges))

    def add_vertex(self, vertice: V) -> int:
        # Además de añadir el vértice, e iniciar sus aristas a [], devuelve un entero con el índice
        self._vertices.append(vertice)
        self._edges.append([])
        return self.vertex_count - 1

    def add_edge(self, edge: Edge) -> None:
        """
        Para añadir una arista u -> v, como estamos trabajando con grafos no dirigidos
        1º Debemos añadir el edge u -> v a la lista de aristas del vértice de índice u
        2º Debemos añadir el edge v -> u a la lista de aristas del vértice de índice v
        Recordemos que la listas de aristas de un vértice con int u, ocupa el lugar u de la lista _edges
        """
        self._edges[edge.u].append(edge)
        self._edges[edge.v].append(edge.reversed())

    # ¡otra forma de añadir un vértice, dados los índices!!!
    def add_edge_by_indices(self, u: int, v: int) -> None:
        """
        ¡No es adecuado, mejor utilizar la anterior!
        Y él ya añadirá los de lados solo...
        self._edges[u].append(Edge(u, v))
        self._edges[v].append(Edge(v, u))
        """
        edge: Edge = Edge(u, v)
        self.add_edge(edge)

    # Add an edge by vertices, looking up vertex indices (convenience method)
    def add_edge_by_vertices(self, vertice_inicial: V, vertice_final: V) -> None:
        u = self._vertices.index(vertice_inicial)
        v = self._vertices.index(vertice_final)
        self.add_edge_by_indices(u, v)

    # Find the vertex at a specific index
    def vertex_at(self, index: int) -> V:
        return self._vertices[index]

    # Find the index of a vertex in the graph
    def index_of(self, vertice: V) -> int:
        return self._vertices.index(vertice)

    # Find the vertices that a vertex at some index is connected to
    def neighbors_for_index(self, index: int) -> List[V]:
        """
        Recordar que el índice realmente nos dice cuál es el número de ítem
        tanto del vértice en la lista de vértices, como el de sus edges, en la lista de edges
        """
        return list(map(self.vertex_at, [edge.v for edge in self._edges[index]]))

    # Look up a vertice's index and find its neighbors (convenience method)
    def neighbors_for_vertex(self, vertice: V) -> List[V]:
        return self.neighbors_for_index(self.index_of(vertice))

    # Return all the edges associated with a vertex at some index
    def edges_for_index(self, index: int) -> List[Edge]:
        return self._edges[index]

    # Look up the index of a vertex and return its edges (convenience method)
    def edges_for_vertex(self, vertice: V) -> List[Edge]:
        return self.edges_for_index(self.index_of(vertice))

    # Make it easy to pretty-print a Graph
    def __str__(self) -> str:
        desc: str = f'El total de vértices es {self.vertex_count}:\n'
        for i in range(self.vertex_count):
            desc += f"{self.vertex_at(i)} -> {self.neighbors_for_index(i)}\n"
        desc += f'En total hay {self.edges_count} aristas\n'
        return desc


if __name__ == "__main__":
    # test basic Graph construction
    city_graph: Graph[str] = Graph(["Seattle", "San Francisco", "Los Angeles", "Riverside",
                                    "Phoenix", "Chicago", "Boston", "New York", "Atlanta",
                                    "Miami", "Dallas", "Houston", "Detroit", "Philadelphia",
                                    "Washington"])
    city_graph.add_edge_by_vertices("Seattle", "Chicago")
    city_graph.add_edge_by_vertices("Seattle", "San Francisco")
    city_graph.add_edge_by_vertices("San Francisco", "Riverside")
    city_graph.add_edge_by_vertices("San Francisco", "Los Angeles")
    city_graph.add_edge_by_vertices("Los Angeles", "Riverside")
    city_graph.add_edge_by_vertices("Los Angeles", "Phoenix")
    city_graph.add_edge_by_vertices("Riverside", "Phoenix")
    city_graph.add_edge_by_vertices("Riverside", "Chicago")
    city_graph.add_edge_by_vertices("Phoenix", "Dallas")
    city_graph.add_edge_by_vertices("Phoenix", "Houston")
    city_graph.add_edge_by_vertices("Dallas", "Chicago")
    city_graph.add_edge_by_vertices("Dallas", "Atlanta")
    city_graph.add_edge_by_vertices("Dallas", "Houston")
    city_graph.add_edge_by_vertices("Houston", "Atlanta")
    city_graph.add_edge_by_vertices("Houston", "Miami")
    city_graph.add_edge_by_vertices("Atlanta", "Chicago")
    city_graph.add_edge_by_vertices("Atlanta", "Washington")
    city_graph.add_edge_by_vertices("Atlanta", "Miami")
    city_graph.add_edge_by_vertices("Miami", "Washington")
    city_graph.add_edge_by_vertices("Chicago", "Detroit")
    city_graph.add_edge_by_vertices("Detroit", "Boston")
    city_graph.add_edge_by_vertices("Detroit", "Washington")
    city_graph.add_edge_by_vertices("Detroit", "New York")
    city_graph.add_edge_by_vertices("Boston", "New York")
    city_graph.add_edge_by_vertices("New York", "Philadelphia")
    city_graph.add_edge_by_vertices("Philadelphia", "Washington")
    print(city_graph)
