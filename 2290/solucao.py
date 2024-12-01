import heapq
class Solution:

    def minimumObstacles(self, grid):

        n = len(grid[0])

        minHeap = [(0, 0, 0)]
        
        m = len(grid)
        visitado = [[float('inf')] * n for _ in range(m)]
        visitado[0][0] = 0

        def exploraCelula(nx, ny, obstaculos):
            novo_Obstaculo = obstaculos + grid[nx][ny]
            if novo_Obstaculo < visitado[nx][ny]:
                visitado[nx][ny] = novo_Obstaculo
                heapq.heappush(minHeap, (novo_Obstaculo, nx, ny))

        while minHeap:
            obstaculos, x, y = heapq.heappop(minHeap)
            
            if x == m - 1 and y == n - 1:
                return obstaculos

            if x - 1 >= 0:
                exploraCelula(x - 1, y, obstaculos)
            
            if x + 1 < m:
                exploraCelula(x + 1, y, obstaculos)
            
            if y - 1 >= 0:
                exploraCelula(x, y - 1, obstaculos)
            
            if y + 1 < n:
                exploraCelula(x, y + 1, obstaculos)
        
        return -1

    
def main():
    solucao = Solution()

    # Caso 1. Saída esperada: 2
    grid = [[0,1,1],[1,1,0],[1,1,0]]
    result = solucao.minimumObstacles(grid)
    print(f"{result}")

    # Caso 2. Saída esperada: 0
    grid = grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
    result = solucao.minimumObstacles(grid)
    print(f"{result}")

main()
