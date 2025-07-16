from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Encontra a soma de três números em nums que está mais próxima do target.
        
        Utiliza a abordagem de dois ponteiros após ordenar o array para encontrar
        eficientemente a combinação de três números cuja soma está mais próxima
        do valor alvo.
        
        Args:
            nums: Lista de números inteiros de tamanho n
            target: Valor alvo para encontrar a soma mais próxima
            
        Returns:
            A soma dos três números que está mais próxima do target
        """
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')
        
        for i in range(n - 2):
            # Otimização: evita duplicatas no primeiro elemento
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # Verifica se encontrou uma soma mais próxima do target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Se a soma atual é igual ao target, retorna imediatamente
                if current_sum == target:
                    return target
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return closest_sum