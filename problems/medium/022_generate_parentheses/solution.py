from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Gera todas as combinações de parênteses bem formados para n pares.

        Utiliza backtracking para construir as combinações válidas de parênteses.
        A cada passo, adiciona um parêntese de abertura '(' se ainda há parênteses disponíveis, ou um parêntese de fechamento ')' se há mais parênteses de abertura que de fechamento na string atual.

        Args:
            n (int): Número de pares de parênteses
            
        Returns:
            List[str]: Lista com todas as combinações válidas de parênteses
        """
        result = []

        def backtrack(current_combination: str, open_count: int, close_count: int) -> None:
            """
            Função axuiliar de backtracking para gerar combinações válidas.

            Args:
                current_combination (str): String atual sendo construída
                open_count (int): Número de parênteses de abertura já adicionados
                close_count (int): Número de parênteses de fechamento já adicionados
            """

            # Caso base: se usarmos todos os n pares de parênteses
            if len(current_combination) == 2 * n:
                result.append(current_combination)
                return
            
            # Adiciona ( se ainda estiver disponível
            if open_count < n:
                backtrack(current_combination + "(", open_count + 1, close_count)

            # Adiciona ) se ainda houver mais para fechar
            if close_count < open_count:
                backtrack(current_combination + ")", open_count, close_count + 1)
            
        backtrack("", 0, 0)
        return result