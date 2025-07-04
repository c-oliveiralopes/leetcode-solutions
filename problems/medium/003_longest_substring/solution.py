class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Problema 3: Longest Substring Without Repeating Characters (https://leetcode.com/problems/longest-substring-without-repeating-characters/)
        Dificuldade: Médio
        Tópicos: Tabela de hash, string, janela deslizante
        
        Abordagem: Sliding Window (janela deslizante) com Hashmap
        - Duas pontas: left(inívio) e right(fim) da janela
        - Armazena o último índice de cada caractere
        - Quando encontramos um caractere duplicado, movemos left para após a última ocorrência
        - Sempre atualizamos o comprimento máximo encontrado
        Complexidade temporal: O(n) | Complexidade espacial: O(Min(M, N))
        """
        if not s:
            return 0

        # Mapa para armazenar o último índice de cada caractere    
        char_index_map = {}
        max_length = 0
        left = 0 # Início da janela

        for right in range(len(s)):
            char = s[right]

            if char in char_index_map and char_index_map[char] >= left:
                left = char_index_map[char] + 1

            char_index_map[char] = right

            current_length = right - left + 1
            max_length = max(max_length, current_length)

        return max_length