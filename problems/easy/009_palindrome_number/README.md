# 9. Palindrome Number

> O desafio consiste em determinar se um número inteiro é um palíndromo, ou seja, se sua leitura é a mesma da esquerda para a direita e vice-versa.

Este repositório contém duas implementações distintas em Python para a solução deste problema, cada uma com suas próprias características de desempenho e estilo.

## Abordagens Implementadas

A seguir, uma análise detalhada das duas soluções propostas.

### 1. Abordagem por Manipulação Aritmética

Uma solução matematicamente pura que reverte o número através de operações de módulo e divisão, operando exclusivamente com tipos inteiros e evitando a sobrecarga da conversão de tipos.

<details>
<summary>Visualizar Código</summary>

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_number = 0
        original = x

        while x > 0:
            reversed_number = reversed_number * 10 + x % 10
            x //= 10

        return original == reversed_number
```

</details>

#### Análise de Complexidade

* **Complexidade Temporal: $O(\log_{10} n)$**
    O tempo de execução é proporcional ao número de dígitos (*d*) do inteiro *n*. Como *d* é aproximadamente $\log_{10}n$, a complexidade é logarítmica, e não linear em relação à magnitude de *n*.

* **Complexidade Espacial: $O(1)$**
    A alocação de memória é constante. Apenas um número fixo de variáveis é utilizado, independentemente do tamanho do número de entrada.

### 2. Abordagem por Manipulação de String

Uma solução idiomática e concisa que se aproveita da expressividade da linguagem Python, convertendo o número para uma string e comparando-a com sua versão invertida.

<details>
<summary>Visualizar Código</summary>

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return str(x) == str(x)[::-1]
```

</details>

#### Análise de Complexidade

* **Complexidade Temporal: $O(\log_{10} n)$**
    As operações de conversão do inteiro para string, a inversão da string e a subsequente comparação têm um custo computacional proporcional ao número de dígitos (*d*) do inteiro.

* **Complexidade Espacial: $O(\log_{10} n)$**
    É necessário alocar memória para armazenar a representação do número em formato de string. O espaço requerido cresce linearmente com o número de dígitos de *n*.

## Detalhes do Desafio

* **Nível:** `Fácil`
* **Tópicos:** `Matemática`
* **Fonte Oficial:** [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/)