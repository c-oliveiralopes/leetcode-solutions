from solution import Solution
sol = Solution()

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Problema 1: Two Sum (https://leetcode.com/problems/two-sum/)
        Dificuldade: Fácil
        Tópicos: Ordenação, tabela de hash
        Estratégia: Hashmap para busca O(n)
        - Para cada número, calculamos o seu complemento (target - num)
        - Se o complemento já foi visto, encontramos a solução
        - Caso contrário, armazenamos o número atual
        Complexidade temporal: O(n) | Complexidade espacial: O(n)
        """
        seen = {}  # número -> índice
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []

def test_solution():
    test_cases = [
        ([2, 7, 11, 15], 9),    # Esperado: [0, 1]
        ([3, 2, 4], 6),         # Esperado: [1, 2]
        ([3, 3], 6),            # Esperado: [0, 1]
        ([-1, -2, -3, -4, -5], -8),  # Esperado: [2, 4]
        ([-3, 4, 3, 90], 0),    # Esperado: [0, 2]
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 19),  # Esperado: [8, 9]
        ([0, 4, 3, 0], 0),      # Esperado: [0, 3]
        ([1, 2, 3, 4, 5], -10), # Esperado: []
        ([1, 2], 5),            # Esperado: []
        ([5, 75, 25], 100),     # Esperado: [1, 2]
        ([1000000, 2000000, 3000000], 5000000),  # Esperado: [1, 2]
        ([5], 5),               # Esperado: []
    ]
    
    print("Testando a solução Two Sum:\n")
    
    for nums, target in test_cases:
        result = sol.twoSum(nums, target)
        print(f"Array: {nums}")
        print(f"Target: {target}")
        print(f"Resultado: {result}")
        
        # Verificar se a solução está correta
        if result:
            soma = nums[result[0]] + nums[result[1]]
            print(f"Verificação: {nums[result[0]]} + {nums[result[1]]} = {soma}")
            if soma == target:
                print("CORRETO")
            else:
                print("INCORRETO")
        else:
            print("Sem solução encontrada")
        
        print("-" * 50)

if __name__ == "__main__":
    test_solution()