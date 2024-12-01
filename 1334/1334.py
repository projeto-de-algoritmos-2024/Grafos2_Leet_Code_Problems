import heapq

class Solution:
    def dijkstra(self, grafo, n, inicio, distanceThreshold):
        distancia = [float('inf')] * n
        distancia[inicio] = 0
        minHeap = [(0, inicio)]

        while minHeap:
            distAtual, noAtual = heapq.heappop(minHeap)

            for vizinho, peso in grafo[noAtual]:
                novaDist = distAtual + peso

                if distancia[vizinho] > novaDist:
                    distancia[vizinho] = novaDist
                    heapq.heappush(minHeap, (novaDist, vizinho))
        
        return sum(1 for d in distancia if d <= distanceThreshold)

    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        def criaGrafo(n, edges):
            grafo = {i: [] for i in range(n)}
            for u, v, peso in edges:
                grafo[u].append((v, peso))
                grafo[v].append((u, peso))
            return grafo
        
        grafo = criaGrafo(n, edges)

        menorQtdCidades = float('inf')
        resultado = -1

        for i in range(n):
            qtdCidadesAcessiveis = self.dijkstra(grafo, n, i, distanceThreshold)
            
            
            if qtdCidadesAcessiveis <= menorQtdCidades:
                menorQtdCidades = qtdCidadesAcessiveis
                resultado = i
        
        return resultado

def main():
    solucao = Solution()

    n = 4
    edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
    distanceThreshold = 4

    result = solucao.findTheCity(n, edges, distanceThreshold)
    print(f"{result}")

    n = 5
    edges = [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]]
    distanceThreshold = 2

    result = solucao.findTheCity(n, edges, distanceThreshold)
    print(f"{result}")

main()