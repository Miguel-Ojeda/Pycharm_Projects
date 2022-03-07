from __future__ import annotations
from edge import Edge
from dataclasses import dataclass


@dataclass
class WeightedEdge(Edge):
    weight: float

    def reversed(self) -> WeightedEdge:
        return WeightedEdge(self.v, self.u, self.weight)

    def __str__(self) -> str:
        return f'{self.u} ({self.weight}) -> {self.v}'

    # so that we can order edges by weight to find the minimum weight edge
    # Lo utilizaremos en el algoritmo de Jarník
    def __lt__(self, other: WeightedEdge) -> bool:
        return self.weight < other.weight

