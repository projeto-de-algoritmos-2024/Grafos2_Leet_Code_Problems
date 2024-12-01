import heapq

class Solution:
    def minimumObstacles(self, grid):

    
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
