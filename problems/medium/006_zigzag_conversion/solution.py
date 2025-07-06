class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Converte uma string em padrão zigzag e retorna a leitura linha por linha.
        
        O algoritmo simula o movimento zigzag distribuindo os caracteres da string em linhas, alternando a direção quando atinge o topo ou fundo do padrão.
        
        Args:
            s (str): String a ser convertida. Deve conter apenas letras inglesas, vírgulas e pontos.
            Comprimento entre 1 e 1000 caracteres.
            numRows (int): Número de linhas do padrão zigzag. Valor entre 1 e 1000.
        
        Returns:
            str: String resultante após aplicar o padrão zigzag e ler linha por linha.
        """
        # Caso especial: se há apenas uma linha, retorna a string original
        if numRows == 1:
            return s
        
        rows = [''] * numRows
        
        # Índice da linha atual e direção do movimento
        current_row = 0
        going_down = False
        
        # Percorre cada caractere da string
        for char in s:
            rows[current_row] += char
            
            # Muda a direção quando atinge o topo ou fundo
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            
            # Move para a próxima linha baseado na direção
            current_row += 1 if going_down else -1

        return ''.join(rows)
