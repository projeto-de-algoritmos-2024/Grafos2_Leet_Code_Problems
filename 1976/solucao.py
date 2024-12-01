import heapq

class Solution:
    def dijkstra(self, grafo, distancia, qtdCaminhos):
        minHeap = [(0, 0)]

        while minHeap:
            d, no = heapq.heappop(minHeap)

            for noVizinho, tempo in grafo[no]:
                novaDist = tempo + d

                if distancia[noVizinho] > novaDist:
                    distancia[noVizinho] = novaDist
                    qtdCaminhos[noVizinho] = qtdCaminhos[no]
                    heapq.heappush(minHeap, (novaDist, noVizinho))

                elif novaDist == distancia[noVizinho]:
                    qtdCaminhos[noVizinho] = (qtdCaminhos[noVizinho] + qtdCaminhos[no]) % (10**9 + 7)
        
        return qtdCaminhos[-1]

    def countPaths(self, n: int, roads: list[list[int]]) -> int:

        distancia = [float('inf')] * n
        qtdCaminhos = [0] * n

        distancia[0] = 0
        qtdCaminhos[0] = 1
    
        def criaGrafo(n, roads):
            grafo = {}
            for i in range(n):
                grafo[i] = []
                
            for u, v, tempo in roads:
                grafo[u].append((v, tempo))
                grafo[v].append((u, tempo))
            
            return grafo
        
        grafo = criaGrafo(n, roads)

        result = self.dijkstra(grafo, distancia, qtdCaminhos)
        return result

def main():

    solucao = Solution()

    # Caso 1. Saída esperada: 4
    n = 7
    roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]

    result = solucao.countPaths(n, roads)
    print(f"{result}")


    # Caso 2. Saída esperada: 1
    n = 2
    roads = [[1,0,10]]

    result = solucao.countPaths(n, roads)
    print(f"{result}")

main()