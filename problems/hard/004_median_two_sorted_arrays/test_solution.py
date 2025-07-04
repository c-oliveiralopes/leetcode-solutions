from solution import Solution

def test_solution():
    solution = Solution()
    # Caso 1: Arrays de tamanhos diferentes
    nums1 = [1, 3]
    nums2 = [2]
    result = solution.findMedianSortedArrays(nums1, nums2)
    print(f"Teste 1 - nums1 = {nums1}, nums2 = {nums2}")
    print(f"Mediana: {result}")
    print(f"Esperado: 2.0")
    print(f"Status: {'✓ PASS' if result == 2.0 else '✗ FAIL'}\n")
    
    # Caso 2: Arrays com mais elementos
    nums1 = [1, 2]
    nums2 = [3, 4]
    result = solution.findMedianSortedArrays(nums1, nums2)
    print(f"Teste 2 - nums1 = {nums1}, nums2 = {nums2}")
    print(f"Mediana: {result}")
    print(f"Esperado: 2.5")
    print(f"Status: {'✓ PASS' if result == 2.5 else '✗ FAIL'}\n")
    
    # Caso 3: Array vazio
    nums1 = []
    nums2 = [1]
    result = solution.findMedianSortedArrays(nums1, nums2)
    print(f"Teste 3 - nums1 = {nums1}, nums2 = {nums2}")
    print(f"Mediana: {result}")
    print(f"Esperado: 1.0")
    print(f"Status: {'✓ PASS' if result == 1.0 else '✗ FAIL'}\n")
    
    # Caso 4: Arrays com elementos duplicados
    nums1 = [1, 1, 3, 3]
    nums2 = [1, 1, 3, 3]
    result = solution.findMedianSortedArrays(nums1, nums2)
    print(f"Teste 4 - nums1 = {nums1}, nums2 = {nums2}")
    print(f"Mediana: {result}")
    print(f"Esperado: 2.0")
    print(f"Status: {'✓ PASS' if result == 2.0 else '✗ FAIL'}\n")
    
    # Caso 5: Arrays com tamanhos muito diferentes
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [6]
    result = solution.findMedianSortedArrays(nums1, nums2)
    print(f"Teste 5 - nums1 = {nums1}, nums2 = {nums2}")
    print(f"Mediana: {result}")
    print(f"Esperado: 3.5")
    print(f"Status: {'✓ PASS' if result == 3.5 else '✗ FAIL'}\n")
    
    # Caso 6: Arrays com números negativos
    nums1 = [-5, -3, -1]
    nums2 = [1, 3]
    result = solution.findMedianSortedArrays(nums1, nums2)
    print(f"Teste 6 - nums1 = {nums1}, nums2 = {nums2}")
    print(f"Mediana: {result}")
    print(f"Esperado: -1.0")
    print(f"Status: {'✓ PASS' if result == -1.0 else '✗ FAIL'}\n")
    
    # Caso 7: Um array com um elemento
    nums1 = [2]
    nums2 = [1, 3, 4]
    result = solution.findMedianSortedArrays(nums1, nums2)
    print(f"Teste 7 - nums1 = {nums1}, nums2 = {nums2}")
    print(f"Mediana: {result}")
    print(f"Esperado: 2.5")
    print(f"Status: {'✓ PASS' if result == 2.5 else '✗ FAIL'}\n")

if __name__ == "__main__":
    print("=== Testando Median of Two Sorted Arrays ===\n")
    test_solution()
    print("=== Fim dos testes ===")