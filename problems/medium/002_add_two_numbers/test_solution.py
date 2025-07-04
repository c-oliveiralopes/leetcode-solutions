import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'utils'))

from typing import Optional
from data_structures import ListNode
from solution import Solution
sol = Solution()

# Funções auxiliares para testes
def create_linked_list(numbers):
    """Cria uma lista ligada a partir de uma lista de números."""
    if not numbers:
        return None

    head = ListNode(numbers[0])
    current = head
    for num in numbers[1:]:
        current.next = ListNode(num)
        current = current.next
    return head

def linked_list_to_list(head):
    """Converte uma lista ligada em uma lista Python."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def test_add_two_numbers():
    """Executa testes para a função addTwoNumbers"""
    solution = Solution()
    
    # Teste 1: Exemplo básico (342 + 465 = 807)
    # l1 = [2,4,3], l2 = [5,6,4] => resultado = [7,0,8]
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    result = sol.addTwoNumbers(l1, l2)
    expected = [7, 0, 8]
    actual = linked_list_to_list(result)
    print(f"Teste 1: {actual} == {expected} -> {'PASS' if actual == expected else 'FAIL'}")
    
    # Teste 2: Números com zeros (0 + 0 = 0)
    l1 = create_linked_list([0])
    l2 = create_linked_list([0])
    result = solution.addTwoNumbers(l1, l2)
    expected = [0]
    actual = linked_list_to_list(result)
    print(f"Teste 2: {actual} == {expected} -> {'PASS' if actual == expected else 'FAIL'}")
    
    # Teste 3: Listas de tamanhos diferentes com carry
    # l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9] => resultado = [8,9,9,9,0,0,0,1]
    l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = create_linked_list([9, 9, 9, 9])
    result = solution.addTwoNumbers(l1, l2)
    expected = [8, 9, 9, 9, 0, 0, 0, 1]
    actual = linked_list_to_list(result)
    print(f"Teste 3: {actual} == {expected} -> {'PASS' if actual == expected else 'FAIL'}")
    
    # Teste 4: Um número de um dígito (5 + 5 = 10)
    l1 = create_linked_list([5])
    l2 = create_linked_list([5])
    result = solution.addTwoNumbers(l1, l2)
    expected = [0, 1]
    actual = linked_list_to_list(result)
    print(f"Teste 4: {actual} == {expected} -> {'PASS' if actual == expected else 'FAIL'}")
    
    # Teste 5: Listas de tamanhos diferentes (99 + 9 = 108)
    l1 = create_linked_list([9, 9])
    l2 = create_linked_list([9])
    result = solution.addTwoNumbers(l1, l2)
    expected = [8, 0, 1]
    actual = linked_list_to_list(result)
    print(f"Teste 5: {actual} == {expected} -> {'PASS' if actual == expected else 'FAIL'}")
    
    # Teste 6: Caso com múltiplos carries consecutivos
    l1 = create_linked_list([1, 8])
    l2 = create_linked_list([0, 2])
    result = solution.addTwoNumbers(l1, l2)
    expected = [1, 0, 1]
    actual = linked_list_to_list(result)
    print(f"Teste 6: {actual} == {expected} -> {'PASS' if actual == expected else 'FAIL'}")
    
    # Teste 7: Lista vazia vs número (edge case)
    l1 = create_linked_list([1])
    l2 = create_linked_list([9, 9])
    result = solution.addTwoNumbers(l1, l2)
    expected = [0, 0, 1]
    actual = linked_list_to_list(result)
    print(f"Teste 7: {actual} == {expected} -> {'PASS' if actual == expected else 'FAIL'}")

if __name__ == "__main__":
    print("Executando testes para Add Two Numbers:")
    print("="*50)
    test_add_two_numbers()
    print("="*50)
    print("Testes concluídos!")