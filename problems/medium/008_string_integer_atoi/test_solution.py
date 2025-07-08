from solution import Solution

def test_myatoi():
    """Testa a função myAtoi com casos essenciais."""
    solution = Solution()
    
    # Casos de teste: (entrada, resultado_esperado)
    casos = [
        ("42", 42),
        ("   -42", -42),
        ("4193 with words", 4193),
        ("words and 987", 0),
        ("", 0),
        ("   ", 0),
        ("+1", 1),
        ("+-12", 0),
        ("91283472332", 2147483647),      # overflow positivo
        ("-91283472332", -2147483648),    # overflow negativo
    ]
    
    print("Testando myAtoi...")
    print("-" * 40)
    
    todos_passaram = True
    
    for entrada, esperado in casos:
        resultado = solution.myAtoi(entrada)
        passou = resultado == esperado
        status = "✓" if passou else "✗"
        
        print(f"{status} '{entrada}' -> {resultado} (esperado: {esperado})")
        
        if not passou:
            todos_passaram = False
    
    print("-" * 40)
    if todos_passaram:
        print("✓ Todos os testes passaram!")
    else:
        print("✗ Alguns testes falharam!")


if __name__ == "__main__":
    test_myatoi()