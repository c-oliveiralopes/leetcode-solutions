import unittest
from solution import Solution

class TestLongestPalindrome(unittest.TestCase):
    """Classe de testes para a solução do problema 'Longest Palindromic Substring'."""
    def setUp(self):
        self.solver = Solution()

    def test_empty_string(self):
        """Testa com uma string vazia."""
        self.assertEqual(self.solver.longestPalindrome(""), "")

    def test_single_character(self):
        """Testa com uma string de um único caractere."""
        self.assertEqual(self.solver.longestPalindrome("a"), "a")

    def test_entire_string_is_palindrome_odd(self):
        """Testa um palíndromo de comprimento ímpar que é a própria string."""
        self.assertEqual(self.solver.longestPalindrome("racecar"), "racecar")
        
    def test_entire_string_is_palindrome_even(self):
        """Testa um palíndromo de comprimento par que é a própria string."""
        self.assertEqual(self.solver.longestPalindrome("aabbaa"), "aabbaa")

    def test_simple_even_palindrome(self):
        """Testa com um palíndromo simples de comprimento par."""
        self.assertEqual(self.solver.longestPalindrome("cbbd"), "bb")

    def test_multiple_valid_answers(self):
        """
        Testa um caso onde múltiplas respostas são válidas ('bab' ou 'aba').
        A implementação pode retornar qualquer uma delas.
        """
        result = self.solver.longestPalindrome("babad")
        self.assertIn(result, ["bab", "aba"])

    def test_palindrome_at_the_end(self):
        """Testa um palíndromo localizado no final da string."""
        self.assertEqual(self.solver.longestPalindrome("workinggnikrow"), "workinggnikrow")
        
    def test_no_palindrome_longer_than_one(self):
        """Testa uma string sem palíndromos de comprimento > 1."""
        # Qualquer caractere único é uma resposta válida.
        self.assertEqual(len(self.solver.longestPalindrome("abcdefg")), 1)

    def test_long_string_with_internal_palindrome(self):
        """Testa uma string longa com um palíndromo interno bem definido."""
        self.assertEqual(self.solver.longestPalindrome("tracecars"), "racecar")

    def test_string_with_all_same_characters(self):
        """Testa uma string composta por um único caractere repetido."""
        self.assertEqual(self.solver.longestPalindrome("aaaaa"), "aaaaa")

if __name__ == '__main__':
    unittest.main(verbosity=2)