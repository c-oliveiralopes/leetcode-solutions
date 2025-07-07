from solution import Solution

def test_solution():
    solution = Solution()
    
    print("=== Testes do Reverse Integer (Python) ===")
    
    # Casos básicos
    print(f"reverse(123) = {solution.reverse(123)}")     # Esperado: 321
    print(f"reverse(-123) = {solution.reverse(-123)}")   # Esperado: -321
    print(f"reverse(120) = {solution.reverse(120)}")     # Esperado: 21
    
    # Casos de overflow
    print(f"reverse(1534236469) = {solution.reverse(1534236469)}")   # Esperado: 0
    print(f"reverse(-1534236469) = {solution.reverse(-1534236469)}") # Esperado: 0
    
    # Casos extremos
    print(f"reverse(0) = {solution.reverse(0)}")         # Esperado: 0
    print(f"reverse(1) = {solution.reverse(1)}")         # Esperado: 1
    print(f"reverse(-1) = {solution.reverse(-1)}")       # Esperado: -1
    
    # Casos no limite
    print(f"reverse(2147483647) = {solution.reverse(2147483647)}")   # Esperado: 0
    print(f"reverse(-2147483648) = {solution.reverse(-2147483648)}") # Esperado: 0
    
    # Casos adicionais
    print(f"reverse(1563847412) = {solution.reverse(1563847412)}")   # Esperado: 0
    print(f"reverse(-2143847412) = {solution.reverse(-2143847412)}") # Esperado: -2147438412

if __name__ == "__main__":
    test_solution()