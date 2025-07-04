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
        seen = {} # número -> índice

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]
            
            seen[num] = i

        return []
