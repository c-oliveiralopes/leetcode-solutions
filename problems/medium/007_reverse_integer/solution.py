class Solution:
    def reverse(self, x: int) -> int:
        """
        Reverte os dígitos de um inteiro de 32 bits com sinal.
        
        Dado um inteiro x de 32 bits com sinal, retorna x com seus dígitos revertidos.
        Se a reversão de x causar que o valor saia do intervalo de inteiros de 32 bits com sinal [-2³¹, 2³¹ - 1], retorna 0.
        
        Parâmetros:
            x (int): Um inteiro de 32 bits com sinal para reverter
            
        Retorna:
            int: O inteiro revertido, ou 0 se ocorrer overflow
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        result = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)
        
        while x:
            digit = x % 10
            x //= 10
            
            # Verifica overflow antes de atualizar result
            if result > (INT_MAX - digit) // 10:
                return 0
            
            result = result * 10 + digit
        
        result *= sign
        
        # Verifica se o resultado final está no range válido
        if result < INT_MIN or result > INT_MAX:
            return 0
        
        return result