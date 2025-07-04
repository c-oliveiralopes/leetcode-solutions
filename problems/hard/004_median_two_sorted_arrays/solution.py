from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Problema 4: Median of Two Sorted Arrays (https://leetcode.com/problems/median-of-two-sorted-arrays/)
        Dificuldade: Difícil
        Tópicos: Array, busca binária, divide e conquista

        Estratégia: Busca binária para encontrar a partição correta
        - Garantimos que nums1 seja o menor array para otimizar a busca
        - Aplicamos busca binária no array menor
        - Particionamos ambos os arrays de forma que a parte esquerda tenha exatamente metade dos elementos
        - Verificamos se max_left1 <= min_right2 e max_left2 <= min_right1
        - Calculamos a mediana baseado na paridade do total de elementos
        Complexidade temporal: O(log(min(m,n))) | Complexidade espacial: O(1)
        """
        # Garante que nums1 seja o menor array para otimizar a busca binária
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = (total) // 2

        left, right = 0, m

        while left <= right:
            partition1 = (left + right) // 2
            partition2 = half - partition1 

            # Elementos máximos da parte esquerda de cada array
            max_left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            max_left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]

            # Elementos mínimos da parte direita de cada array
            min_right1 = float('inf') if partition1 == m else nums1[partition1]
            min_right2 = float('inf') if partition2 == n else nums2[partition2]

            # Verifica se encontrou a partição correta
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                if total % 2 == 0:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
                else:
                    return min(min_right1, min_right2)
                
            elif max_left1 > min_right2:
                right = partition1 - 1
            
            else:
                left = partition1 + 1

        raise ValueError("Input arrays must be sorted")