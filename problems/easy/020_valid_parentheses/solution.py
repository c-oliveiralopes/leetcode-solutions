class Solution:
    def isValid(self, s: str) -> bool:
        """
        Verifica se uma string contendo parênteses, colchetes e chaves está válida.
        
        Uma string é considerada válida se:
        1. Cada abertura tem seu fechamento correspondente do mesmo tipo
        2. Os fechamentos ocorrem na ordem correta (LIFO - Last In, First Out)
        3. Não há fechamentos sem aberturas correspondentes
        
        Args:
            s (str): String contendo apenas os caracteres '(', ')', '{', '}', '[', ']'
            
        Returns:
            bool: True se a string for válida, False caso contrário
        """
        # Dicionário que mapeia cada fechamento para sua abertura correspondente
        mapeamento = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        # Pilha para armazenar as aberturas encontradas
        pilha = []
        
        # Percorre cada caractere da string
        for caractere in s:
            # Se for um caractere de fechamento
            if caractere in mapeamento:
                # Verifica se a pilha está vazia ou se o topo não corresponde
                if not pilha or pilha.pop() != mapeamento[caractere]:
                    return False
            else:
                # Se for um caractere de abertura, adiciona à pilha
                pilha.append(caractere)
        
        # A string é válida apenas se a pilha estiver vazia (todas as aberturas foram fechadas)
        return len(pilha) == 0