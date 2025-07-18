from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Encontra todas as quádruplas únicas no array que somam ao valor alvo.
        
        Utiliza a técnica de dois ponteiros após ordenação para evitar duplicatas
        e otimizar a busca. O algoritmo fixa dois elementos e usa dois ponteiros
        para encontrar os outros dois elementos que completam a soma.
        
        Args:
            nums: Lista de inteiros onde buscar as quádruplas
            target: Valor alvo para a soma das quádruplas
            
        Returns:
            Lista contendo todas as quádruplas únicas que somam ao target
            
        Complexidade:
            Temporal: O(n³) - três loops aninhados
            Espacial: O(1) - apenas variáveis auxiliares (desconsiderando o espaço da resposta)
        """
        n = len(nums)
        if n < 4:
            return []
        
        # Ordena o array para facilitar a busca e evitar duplicatas
        nums.sort()
        result = []
        
        # Primeiro loop: fixa o primeiro elemento
        for i in range(n - 3):
            # Pula elementos duplicados no primeiro índice
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Otimização: se a soma mínima possível for maior que target
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            
            # Otimização: se a soma máxima possível for menor que target
            if nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target:
                continue
            
            # Segundo loop: fixa o segundo elemento
            for j in range(i + 1, n - 2):
                # Pula elementos duplicados no segundo índice
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # Otimização: se a soma mínima possível for maior que target
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                
                # Otimização: se a soma máxima possível for menor que target
                if nums[i] + nums[j] + nums[n - 1] + nums[n - 2] < target:
                    continue
                
                # Usa dois ponteiros para encontrar os outros dois elementos
                left, right = j + 1, n - 1
                
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if current_sum == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Pula elementos duplicados no ponteiro esquerdo
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        
                        # Pula elementos duplicados no ponteiro direito
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        
                        left += 1
                        right -= 1
                    elif current_sum < target:
                        left += 1
                    else:
                        right -= 1
        
        return result