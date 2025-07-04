from solution import Solution
sol = Solution()

def test_solution():
    test_cases = [
        "abcabcbb",  # Esperado: 3
        "bbbbb",     # Esperado: 1
        "pwwkew",    # Esperado: 3
        "",          # Esperado: 0
        "au",        # Esperado: 2
        "dvdf",      # Esperado: 3
    ]

    print("Testando a solução:\n")
    for s in test_cases:
        result1 = sol.lengthOfLongestSubstring(s)
        print(f"String: '{s}'")
        print(f"Resultado: {result1}")
        print("-" * 30)

if __name__ == "__main__":
    test_solution()