class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Converte um numeral romano para inteiro.
        
        Esta solução utiliza um dicionário para mapear os símbolos romanos
        aos seus valores e processa a string da direita para a esquerda.
        Quando um símbolo tem valor menor que o anterior, ele é subtraído;
        caso contrário, é somado.
        
        Args:
            s (str): String contendo o numeral romano válido
            
        Returns:
            int: Valor inteiro correspondente ao numeral romano
        """
        # Mapeamento dos símbolos romanos para seus valores
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        # Processa a string da direita para a esquerda
        for char in reversed(s):
            current_value = roman_values[char]
            
            # Se o valor atual é menor que o anterior, subtrai
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
                
            prev_value = current_value
            
        return total