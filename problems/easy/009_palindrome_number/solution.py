class Solution:
    def isPalindrome(self, x: int) -> bool:
        """Verifica se um número inteiro é um palíndromo.
        
        Esta abordagem utiliza um método matemático para reverter o número.
        O algoritmo progressivamente extrai o último dígito do número original e o anexa a uma nova variável que conterá o número invertido.

        Inclui otimizações para descartar rapidamente casos inválidos, como números negativos ou múltiplos de 10 (exceto o próprio zero), que, por natureza, não podem ser palíndromos.

        Args:
            x (int): O número inteiro a ser verificado

        Returns:
            bool: Retorna `True` se o número for um palíndromo, `False` caso contrário.
        """
        # Otimização: Números negativos ou terminados em zero (e não sendo zero) não são palíndromos.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        # Otimização: números de um dígito são, por definição, palíndromos
        if x < 10:
            return True
        
        # Inversão matemática
        original = x
        reversed_number = 0

        while x > 0:
            # Qualquer número inteiro dividido por 10 terá como resto o seu último dígito (x % 10)
            # Adiciona um zero ao final do número, abrindo espaço para o novo dígito (reversed_number * 10)
            reversed_number = reversed_number * 10 + x % 10
            x //= 10

        return original == reversed_number