# 10. Correspondência de Expressões Regulares
<div align="center">
    <img src="https://img.shields.io/badge/LeetCode-Problem%20Link-black?style=for-the-badge&logo=leetcode" alt="[Link para o problema no LeetCode](https://leetcode.com/problems/regular-expression-matching)">
    <img src="https://img.shields.io/badge/Difficulty-Hard-critical?style=for-the-badge" alt="Dificuldade Hard">
    <img src="https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python" alt="Linguagem Python">
    <img src="https://img.shields.io/badge/Category-Dynamic%20Programming-9cf?style=for-the-badge" alt="Categoria Dynamic Programming">
</div>

<br>

## Problema

> Given an input string `s` and a pattern `p`, implement regular expression matching with support for `.` and `*` where:
> - `.` Matches any single character.​​​​
> - `*` Matches zero or more of the preceding element.
>
> The matching should cover the **entire** input string (not partial).

## Abordagem

O desafio central deste problema reside no operador `*`, que introduz múltiplas possibilidades de ramificação a cada ocorrência. Essa característica, onde a solução de um problema depende de soluções para subproblemas menores e sobrepostos, torna a **Programação Dinâmica (PD)** a abordagem ideal.

Esta solução emprega uma estratégia de **PD Top-Down** (de cima para baixo), também conhecida como **Recursão com Memoização**.

Definimos uma função recursiva, `dfs(i, j)`, que responde à pergunta: "O sufixo da string `s` a partir do índice `i` corresponde ao sufixo do padrão `p` a partir do índice `j`?".

Para evitar a complexidade de tempo exponencial decorrente do recálculo dos mesmos estados, utilizamos um cache (um mapa de hash) para armazenar o resultado de cada par `(i, j)`.

A lógica procede da seguinte forma:
1.  **Caso Base:** Se esgotarmos o padrão (`j == len(p)`), a correspondência só é bem-sucedida se também tivermos esgotado a string (`i == len(s)`).
2.  **Tratamento do `*`:** Se `p[j+1]` for `*`, temos duas escolhas:
    -   **Zero Ocorrências:** Ignorar a parte `p[j]*` e verificar se `s[i:]` corresponde a `p[j+2:]`.
    -   **Uma ou Mais Ocorrências:** Se os caracteres atuais corresponderem, consumimos um caractere de `s` e tentamos novamente o *mesmo* caractere do padrão `p[j]` (pois `*` permite múltiplas correspondências).
3.  **Correspondência Padrão:** Se não houver `*`, uma correspondência exige que os caracteres atuais sejam compatíveis, e então avançamos ambos os ponteiros (`i+1`, `j+1`).

A resposta final é o resultado da chamada inicial `dfs(0, 0)`.

## Solução

<details>
<summary>Clique para expandir a solução</summary>

```python
class Solution:
    """
    Encapsula a solução para o problema de Correspondência de Expressões Regulares.
    """

    def isMatch(self, s: str, p: str) -> bool:
        """Determina se a string de entrada corresponde inteiramente ao padrão.

        Esta implementação utiliza uma abordagem de programação dinâmica top-down
        (recursão com memoização) para resolver o problema de forma eficiente.
        A complexidade introduzida pelos operadores '.' e '*' é gerenciada
        através da exploração de subproblemas, cujos resultados são armazenados
        em cache para evitar recálculos.

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
            if j == len(p):
                return i == len(s)

            # 3. Análise da Correspondência Atual
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

            # 4. Lógica do Operador '*'
            if j + 1 < len(p) and p[j + 1] == '*':
                result = dfs(i, j + 2) or (first_match and dfs(i + 1, j))
            
            # 5. Lógica da Correspondência Padrão
            elif first_match:
                result = dfs(i + 1, j + 1)
            
            else:
                result = False
            
            cache[(i, j)] = result
            return result

        return dfs(0, 0)
````

### Análise de Complexidade

-   **Complexidade de Tempo:** $O(M \times N)$
    -   Onde $M$ é o comprimento de `s` e $N$ é o comprimento de `p`. Graças à memoização, cada um dos $M \times N$ estados possíveis é computado apenas uma vez.

-   **Complexidade de Espaço:** $O(M \times N)$
    -   Devido ao espaço requerido pelo cache da recursão para armazenar os resultados de todos os estados.