import heapq
from typing import List

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.grafo = {i: [] for i in range(n)}
        for u, v, w in edges:
            self.addEdge([u, v, w])

    def addEdge(self, edge: List[int]) -> None:
        u, v, w = edge
        self.grafo[u].append((v, w))

    def shortestPath(self, node1: int, node2: int) -> int:
        fila_prioridade = [(0, node1)]
        distancias = [float('inf')] * self.n
        distancias[node1] = 0

        while fila_prioridade:
            d, no = heapq.heappop(fila_prioridade)

            if no == node2:
                return d

            if d > distancias[no]:
                continue

            for vizinho, peso in self.grafo[no]:
                nova_distancia = d + peso
                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    heapq.heappush(fila_prioridade, (nova_distancia, vizinho))

        return -1 if distancias[node2] == float('inf') else distancias[node2]

def main():
    arestas = [
        [0, 2, 5],
        [0, 1, 2],
        [1, 2, 1],
        [3, 0, 3]
    ]

    grafo = Graph(4, arestas)

    result1 = grafo.shortestPath(3, 2)
    print(result1)

    result2 = grafo.shortestPath(0, 3)
    print(result2)

    grafo.addEdge([1, 3, 4])

    result3 = grafo.shortestPath(0, 3)
    print(result3)

if __name__ == "__main__":
    main()