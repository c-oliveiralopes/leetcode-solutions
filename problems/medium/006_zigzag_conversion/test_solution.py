import unittest
from solution import Solution

class TestZigzagConversion(unittest.TestCase):
    """
    Suíte de testes para o método `convert` da classe Solution.
    """

    def setUp(self):
        """
        Prepara o ambiente para cada teste, instanciando a classe Solution.
        Este método é executado antes de cada método de teste.
        """
        self.solver = Solution()

    def test_example_case_1(self):
        """Testa o exemplo clássico: 'PAYPALISHIRING' com 3 linhas."""
        self.assertEqual(self.solver.convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")

    def test_example_case_2(self):
        """Testa o segundo exemplo clássico: 'PAYPALISHIRING' com 4 linhas."""
        self.assertEqual(self.solver.convert("PAYPALISHIRING", 4), "PINALSIGYAHRPI")

    def test_single_row(self):
        """Testa o caso de borda com numRows = 1."""
        self.assertEqual(self.solver.convert("PYTHON", 1), "PYTHON")

    def test_string_shorter_than_rows(self):
        """Testa quando a string é mais curta que o número de linhas."""
        self.assertEqual(self.solver.convert("ABC", 5), "ABC")

    def test_rows_equal_to_string_length(self):
        """Testa quando numRows é igual ao comprimento da string."""
        self.assertEqual(self.solver.convert("ABCDE", 5), "ABCDE")

    def test_single_character_string(self):
        """Testa com uma string de um único caractere."""
        self.assertEqual(self.solver.convert("A", 2), "A")
    
    def test_string_with_punctuation(self):
        """Testa com uma string contendo vírgulas e pontos, conforme permitido."""
        self.assertEqual(self.solver.convert("A,B.C", 2), "ABC,.")

    def test_two_rows(self):
        """Testa o caso com duas linhas, que separa caracteres pares e ímpares."""
        self.assertEqual(self.solver.convert("THISISATEST", 2), "TIIAETHSSTS")
if __name__ == '__main__':
    unittest.main(verbosity=2)