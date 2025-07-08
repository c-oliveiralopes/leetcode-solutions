class Solution:
    def myAtoi(self, s: str) -> int:
        """
        Converte uma string para um inteiro de 32 bits com sinal.
        
        Implementa o algoritmo myAtoi que segue os seguintes passos:
        1. Ignora espaços em branco no início da string
        2. Determina o sinal verificando se o próximo caractere é '-' ou '+'
        3. Converte os dígitos consecutivos em inteiro, parando no primeiro não-dígito
        4. Aplica arredondamento se o valor estiver fora do range de 32 bits
        
        Args:
            s (str): String a ser convertida em inteiro
            
        Returns:
            int: Inteiro de 32 bits com sinal no range [-2^31, 2^31 - 1]
        """
        # Definindo os limites do inteiro de 32 bits
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # 1. Ignorar os espaços em branco
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1

        if i >= len(s):
            return 0
        
        # 2. Determinar o sinal
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        # 3. Converter os dígitos
        result = 0
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])

            # Verificar overflow antes de adicionar o dígito
            # Se result > INT_MAX // 10, então result * 10 > INT_MAX
            # Se result == INT_MAX // 10 e digit > INT_MAX % 10, então result * 10 + digit > INT_MAX
            if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > INT_MAX % 10):
                return INT_MAX if sign == 1 else INT_MIN
            
            result = result * 10 + digit
            i += 1

        # 4. Aplica o sinal e verifica os limites
        result *= sign

        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN
        
        return result