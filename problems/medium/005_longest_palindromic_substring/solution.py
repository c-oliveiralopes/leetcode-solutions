class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Encontra o maior palíndromo em uma string usando o método 'expand around centers'.
        
        Args:
            s: String de entrada contendo apenas dígitos e letras inglesas
            
        Returns:
            String representando o maior palíndromo encontrado
        """
        # Verifica se a string é vazia ou tem apenas um caractere
        if len(s) < 2:
            return s
        
        start, end = 0, 0
        
        # Itera sobre cada caractere da string
        for i in range(len(s)):
            # Expande ao redor do centro para palíndromos de comprimento ímpar
            len1 = self._expand_around_center(s, i, i)
            # Expande ao redor do centro para palíndromos de comprimento par
            len2 = self._expand_around_center(s, i, i + 1)
            # Obtém o comprimento máximo dos dois casos
            max_len = max(len1, len2)
            
            # Atualiza os índices de início e fim se um palíndromo maior for encontrado
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        
        # Retorna o maior palíndromo encontrado
        return s[start:end + 1]
    
    def _expand_around_center(self, s: str, left: int, right: int) -> int:
        """
        Expande ao redor do centro para encontrar o comprimento do palíndromo.
        
        Args:
            s: String de entrada
            left: Índice da esquerda do centro
            right: Índice da direita do centro
            
        Returns:
            Comprimento do palíndromo encontrado
        """
        # Expande enquanto os caracteres forem iguais e estivermos dentro dos limites
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        # Retorna o comprimento do palíndromo (right - left - 1)
        return right - left - 1