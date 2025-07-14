from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Encontra o prefixo comum mais longo entre um array de strings.
        
        Esta solução utiliza comparação vertical, verificando caractere por caractere
        em todas as strings simultaneamente até encontrar uma divergência.
        
        Args:
            strs (List[str]): Lista de strings para encontrar o prefixo comum
            
        Returns:
            str: O prefixo comum mais longo entre todas as strings
            
        Raises:
            Retorna string vazia se não houver prefixo comum ou se a lista estiver vazia
        """
        if not strs or not strs[0]:
            return ""
        
        # Itera através de cada posição de caractere
        for i in range(len(strs[0])):
            char = strs[0][i]
            
            # Verifica se o caractere atual é igual em todas as strings
            for j in range(1, len(strs)):
                # Se chegamos ao fim de alguma string ou caracteres diferentes
                if i >= len(strs[j]) or strs[j][i] != char:
                    return strs[0][:i]
        
        # Se chegamos aqui, a primeira string é o prefixo comum
        return strs[0]