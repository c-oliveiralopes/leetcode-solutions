class Solution:
    """
    Encapsula a solução para o problema de Regular Expression Matching.
    """

    def isMatch(self, s: str, p: str) -> bool:
        """Determina se a string de entrada corresponde inteiramente ao padrão.

        Esta implementação utiliza uma abordagem de programação dinâmica top-down,
        conhecida como recursão com memoização, para resolver o problema de
        forma eficiente. A complexidade introduzida pelos operadores '.' e '*'
        é gerenciada através da exploração de subproblemas, cujos resultados
        são armazenados em cache para evitar recálculos.

        Args:
            s: A string de entrada a ser validada.
            p: O padrão de expressão regular, contendo letras, '.' e '*'.

        Returns:
            True se a string 's' corresponder completamente ao padrão 'p',
            False caso contrário.
        """
        # O cache é fundamental para a memoização, armazenando os resultados
        # dos subproblemas já resolvidos no formato (índice_s, índice_p) -> bool.
        cache = {}

        def dfs(i: int, j: int) -> bool:
            """Executa a busca em profundidade recursiva para validar os sufixos.

            Esta função aninhada é o núcleo da solução, verificando se o
            sufixo s[i:] corresponde ao sufixo p[j:].

            Args:
                i: O índice atual na string de entrada 's'.
                j: O índice atual no padrão 'p'.

            Returns:
                O resultado booleano da correspondência para o estado (i, j).
            """
            # 1. Verificação do cache (Memoização)
            if (i, j) in cache:
                return cache[(i, j)]

            # 2. Caso Base: O padrão foi totalmente consumido.
            # A correspondência é bem-sucedida somente se a string também foi.
            if j == len(p):
                return i == len(s)

            # 3. Análise da Correspondência Atual
            # 'first_match' avalia se os caracteres atuais são compatíveis.
            # A verificação 'i < len(s)' é crucial para evitar erros de índice.
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

            # 4. Lógica do Operador '*'
            # Se o próximo caractere do padrão for '*', a lógica se bifurca.
            if j + 1 < len(p) and p[j + 1] == '*':
                # Opção A: Ignorar o padrão 'p[j]*' (zero ocorrências).
                # Avançamos duas posições no padrão.
                # Opção B: Usar o padrão 'p[j]*' (uma ou mais ocorrências).
                # Requer que 'first_match' seja verdadeiro e consome um
                # caractere da string, mantendo a posição no padrão.
                result = dfs(i, j + 2) or (first_match and dfs(i + 1, j))
            
            # 5. Lógica da Correspondência Padrão
            elif first_match:
                # Se os caracteres correspondem e não há '*', avançamos em ambos.
                result = dfs(i + 1, j + 1)
            
            else:
                # Se nenhuma das condições acima for atendida, a correspondência falha.
                result = False
            
            # Armazena o resultado no cache antes de retornar.
            cache[(i, j)] = result
            return result

        # Ponto de entrada da recursão, começando do início de ambas as sequências.
        return dfs(0, 0)