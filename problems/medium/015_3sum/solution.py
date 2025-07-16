from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Encontra todos os triplets únicos na array que somam zero.
        
        Utiliza a abordagem de dois ponteiros após ordenar a array.
        Para cada elemento fixo, busca os dois outros elementos que
        completam a soma zero usando dois ponteiros que se movem
        das extremidades para o centro.
        
        Args:
            nums: Lista de números inteiros
            
        Returns:
            Lista de listas contendo todos os triplets únicos que somam zero
        """
        # Array muito pequena não pode ter triples
        if len(nums) < 3:
            return []
        
        # Ordenar facilita a eliminação de duplicatas e permite usar dois ponteiros
        nums.sort()
        result = []
        
        # Iterar através de cada elemento como primeiro elemento do triplet
        for i in range(len(nums) - 2):
            # Otimização: se o menor número é positivo, não há como somar zero
            if nums[i] > 0:
                break
            
            # Pular duplicatas para o primeiro elemento
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Usar dois ponteiros para encontrar os outros dois elementos
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    # Triplet encontrado
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Pular duplicatas para o segundo elemento
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    # Pular duplicatas para o terceiro elemento
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Mover ambos os ponteiros após encontrar um triplet válido
                    left += 1
                    right -= 1
                    
                elif current_sum < 0:
                    # Soma muito pequena, mover ponteiro esquerdo para aumentar
                    left += 1
                else:
                    # Soma muito grande, mover ponteiro direito para diminuir
                    right -= 1
        
        return result