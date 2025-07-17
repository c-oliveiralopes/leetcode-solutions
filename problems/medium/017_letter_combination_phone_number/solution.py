from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Retorna todas as combinações possíveis de letras que os dígitos podem representar.
        
        Utiliza o mapeamento tradicional de um teclado telefônico onde cada dígito (2-9)
        corresponde a um conjunto de letras. Implementa backtracking para gerar todas
        as combinações possíveis.
        
        Args:
            digits (str): String contendo dígitos de 2-9 inclusive
            
        Returns:
            List[str]: Lista com todas as combinações possíveis de letras
        """
        if not digits:
            return []
        
        # Mapeamento dos dígitos para letras (teclado telefônico)
        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        result = []
        
        def backtrack(index: int, current_combination: str) -> None:
            """
            Função auxiliar recursiva que implementa backtracking.
            
            Args:
                index (int): Índice atual no string digits
                current_combination (str): Combinação atual sendo construída
            """
            # Caso base: se processamos todos os dígitos
            if index == len(digits):
                result.append(current_combination)
                return
            
            # Pega as letras correspondentes ao dígito atual
            current_digit = digits[index]
            letters = phone_map[current_digit]
            
            # Tenta cada letra possível para o dígito atual
            for letter in letters:
                backtrack(index + 1, current_combination + letter)
        
        backtrack(0, "")
        return result