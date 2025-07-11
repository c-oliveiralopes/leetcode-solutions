class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) < 2:
            raise ValueError("A lista deve conter pelo menos 2 elementos")
    
        left = 0
        right = len(height) - 1
        max_water = 0
    
        while left < right:
            # Calcula a área atual: largura × altura mínima
            width = right - left
            current_area = width * min(height[left], height[right])
        
        # Atualiza a área máxima
            max_water = max(max_water, current_area)
        
        # Move o ponteiro da linha mais baixa
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
    
        return max_water