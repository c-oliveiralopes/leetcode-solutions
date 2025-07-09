class Solution:
    def isPalindrome(self, x: int) -> bool:
        """Verifica se um número inteiro é um palíndromo.
        
        Esta implementação aborda o problema através da conversão do número para seu formato de string.
        A verificação é realizada comparando-se a string original com sua versão invertida, obtida pela técnica do fatiamento (slicing) `[::-1]`.

        Por definição, número negativos são tratados como não palíndromos.

        Args:
            x (int): O número inteiro a ser verificado.
        
        Returns: 
            bool: `True` se o número for um palíndromo, `False` caso contrário.
        """
        if x < 0: return False
        # Slicing reverso [início:fim:passo]
        return str(x) == str(x)[::-1]